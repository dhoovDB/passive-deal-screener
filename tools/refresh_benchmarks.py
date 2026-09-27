#!/usr/bin/env python3
"""Pull and compute every market figure the benchmark snapshots carry.

Maintenance tool for this repo only - not part of the skill and not in the
upstream PR payload (it makes network calls; the shipped scripts never do).
One run replaces the two market-data steps of the refresh procedure in
`references/data/README.md`:

  * Treasury curve  - FRED daily closes for DGS3MO / DGS2 / DGS10
  * ETF figures     - Yahoo Finance dividend-adjusted daily closes, from which
                      trailing 5yr / 10yr annualized total return, 10yr
                      annualized vol, and full-history worst drop are computed

It prints the figures, the constants block for `scripts/benchmark_comparator.py`,
and what changed versus that script's current constants. It writes nothing:
the snapshot prose and `05` are updated by hand from this output. The two
non-market sources (NCREIF via IREI, Preqin via CAIS) remain manual lookups.

Usage:
    python tools/refresh_benchmarks.py                  # as of the latest quarter-end
    python tools/refresh_benchmarks.py --as-of 2026-06-30
    python tools/refresh_benchmarks.py --self-check     # offline check of the math

stdlib-only.
"""

import argparse
import csv
import datetime as dt
import importlib.util
import io
import json
import math
import os
import statistics
import sys
import urllib.request


# --------------------------------------------------------------------------- #
# Data (config only - no logic)
# --------------------------------------------------------------------------- #

TICKERS = ["SPY", "VTI", "VNQ", "IYR", "LQD", "HYG", "PFF", "PRIV"]
FRED_SERIES = {"3mo": "DGS3MO", "2yr": "DGS2", "10yr": "DGS10"}
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=" + ",".join(FRED_SERIES.values())
YAHOO_URL = ("https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
             "?period1=0&period2={period2}&interval=1d")
# Each source accepts a different client identity: Yahoo rejects non-browser
# agents, while FRED drops connections that claim to be a browser.
FRED_USER_AGENT = "passive-deal-screener-refresh/1.0"
YAHOO_USER_AGENT = "Mozilla/5.0"
TRADING_DAYS = 252
COMPARATOR_SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 os.pardir, "scripts", "benchmark_comparator.py")


# --------------------------------------------------------------------------- #
# Pure calculation core (same input -> same output, no side effects)
# A series is a date-sorted list of (datetime.date, adjusted close).
# --------------------------------------------------------------------------- #

def latest_quarter_end(today):
    """The most recent calendar quarter-end strictly before `today`."""
    q_month = ((today.month - 1) // 3) * 3  # 0, 3, 6, 9
    if q_month == 0:
        return dt.date(today.year - 1, 12, 31)
    return dt.date(today.year, q_month + 1, 1) - dt.timedelta(days=1)


def years_before(day, years):
    """Same calendar date `years` earlier (Feb 29 falls back to Feb 28)."""
    try:
        return day.replace(year=day.year - years)
    except ValueError:
        return day.replace(year=day.year - years, day=28)


def close_on_or_before(series, day):
    """Last (date, close) on or before `day`, or None."""
    found = None
    for point in series:
        if point[0] > day:
            break
        found = point
    return found


def annualized_return(series, end, years):
    """Annualized total return (%) over `years` to `end`, or None when the
    series doesn't reach back far enough (first close > a week after start)."""
    start = years_before(end, years)
    a, b = close_on_or_before(series, start), close_on_or_before(series, end)
    if a is None or b is None or series[0][0] > start + dt.timedelta(days=7):
        return None
    span = (b[0] - a[0]).days / 365.25
    return ((b[1] / a[1]) ** (1.0 / span) - 1.0) * 100.0


def annualized_vol(series, end, years):
    """Annualized std-dev (%) of daily log returns over `years` to `end`, or None
    when the series doesn't cover the window."""
    start = years_before(end, years)
    if series[0][0] > start + dt.timedelta(days=7):
        return None
    closes = [v for d, v in series if start <= d <= end]
    rets = [math.log(b / a) for a, b in zip(closes, closes[1:])]
    if len(rets) < 2:
        return None
    return statistics.stdev(rets) * math.sqrt(TRADING_DAYS) * 100.0


def worst_drop(series, end):
    """(largest peak-to-trough fall %, trough date) over the full series to `end`."""
    peak, drop, trough = 0.0, 0.0, None
    for d, v in series:
        if d > end:
            break
        peak = max(peak, v)
        if v / peak - 1.0 < drop:
            drop, trough = v / peak - 1.0, d
    return drop * 100.0, trough


def since_inception(series, end):
    """(annualized %, first date) from the first close to `end`."""
    first, last = series[0], close_on_or_before(series, end)
    span = (last[0] - first[0]).days / 365.25
    return ((last[1] / first[1]) ** (1.0 / span) - 1.0) * 100.0, first[0]


def etf_figures(series, end):
    """Every figure the ETF snapshot carries, for one ticker."""
    drop, trough = worst_drop(series, end)
    incep, first = since_inception(series, end)
    return {
        "five_yr": annualized_return(series, end, 5),
        "ten_yr": annualized_return(series, end, 10),
        "vol_10yr": annualized_vol(series, end, 10),
        "worst_drop": drop,
        "trough": trough,
        "since_inception": incep,
        "first_date": first,
    }


def latest_fred_values(rows, end):
    """{point: (date, value)} - the latest non-empty close on or before `end`
    for each series. `rows` is a list of dicts from the FRED CSV."""
    out = {}
    for point, series_id in FRED_SERIES.items():
        for row in rows:
            day = dt.date.fromisoformat(row["observation_date"])
            value = row.get(series_id, "")
            if day <= end and value not in ("", "."):
                out[point] = (day, float(value))
    return out


def parse_yahoo_chart(payload):
    """Date-sorted [(date, adjusted close)] from a Yahoo chart response."""
    result = payload["chart"]["result"][0]
    stamps = result["timestamp"]
    adj = result["indicators"]["adjclose"][0]["adjclose"]
    return [(dt.datetime.fromtimestamp(t, tz=dt.timezone.utc).date(), v)
            for t, v in zip(stamps, adj) if v]


def constant_changes(current, new):
    """[(name, old, new)] for every constant whose rounded value differs."""
    return [(k, current.get(k), v) for k, v in new.items()
            if current.get(k) is None or round(current[k], 2) != round(v, 2)]


# --------------------------------------------------------------------------- #
# I/O boundary (network, file loading, printing)
# --------------------------------------------------------------------------- #

def fetch(url, user_agent):
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def load_comparator_constants():
    """COMPARATORS / TREASURY from the shipped script, or None if absent."""
    if not os.path.exists(COMPARATOR_SCRIPT):
        return None
    spec = importlib.util.spec_from_file_location("benchmark_comparator", COMPARATOR_SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.COMPARATORS, mod.TREASURY


def pct(x, width=7):
    return f"{'n/a':>{width}}" if x is None else f"{x:>{width - 1}.2f}%"


def main(argv=None):
    p = argparse.ArgumentParser(description="Pull FRED + Yahoo data and compute the benchmark snapshot figures.")
    p.add_argument("--as-of", type=dt.date.fromisoformat,
                   help="ETF quarter-end date, YYYY-MM-DD (default: latest quarter-end)")
    p.add_argument("--json", action="store_true", help="Emit JSON instead of tables")
    p.add_argument("--self-check", action="store_true", help="Offline check of the calculations and exit")
    args = p.parse_args(argv)
    if args.self_check:
        return _self_check()

    as_of = args.as_of or latest_quarter_end(dt.date.today())
    period2 = int(dt.datetime.combine(as_of + dt.timedelta(days=1), dt.time(),
                                      tzinfo=dt.timezone.utc).timestamp())
    try:
        fred_rows = list(csv.DictReader(io.StringIO(fetch(FRED_URL, FRED_USER_AGENT))))
        treasury = latest_fred_values(fred_rows, dt.date.today())
        etfs = {}
        for t in TICKERS:
            chart = json.loads(fetch(YAHOO_URL.format(ticker=t, period2=period2), YAHOO_USER_AGENT))
            etfs[t] = etf_figures(parse_yahoo_chart(chart), as_of)
    except (OSError, ValueError, KeyError, IndexError, TypeError) as e:
        print(f"error: data pull failed - {e}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({"as_of": str(as_of),
                          "treasury": {k: {"date": str(d), "pct": v} for k, (d, v) in treasury.items()},
                          "etfs": {t: {k: (str(v) if isinstance(v, dt.date) else v) for k, v in f.items()}
                                   for t, f in etfs.items()}}, indent=2))
        return 0

    print(f"Treasury curve (FRED, latest daily close)")
    for point, (day, value) in treasury.items():
        print(f"  {point:<5} {value:.2f}%   {day}")
    print(f"\nETF figures to {as_of} (Yahoo dividend-adjusted daily closes)")
    print(f"  {'Ticker':<6} {'5yr':>7} {'10yr':>7} {'Vol10y':>7} {'Worst':>7}  Trough      History from")
    for t, f in etfs.items():
        print(f"  {t:<6} {pct(f['five_yr'])} {pct(f['ten_yr'])} {pct(f['vol_10yr'])} "
              f"{pct(f['worst_drop'])}  {f['trough']}  {f['first_date']}")
        if f["ten_yr"] is None:
            print(f"         since inception: {f['since_inception']:.2f}% annualized")

    new_ten = {t: round(f["ten_yr"], 2) for t, f in etfs.items() if f["ten_yr"] is not None}
    new_treasury = {k: round(v, 2) for k, (_, v) in treasury.items()}
    print("\nConstants for scripts/benchmark_comparator.py:")
    print(f'  LAST_UPDATED = "{dt.date.today()}"')
    print(f"  ten_yr: " + ", ".join(f"{t} {v:.2f}" for t, v in new_ten.items()))
    print(f"  TREASURY = {new_treasury}")

    current = load_comparator_constants()
    if current is not None:
        comparators, treasury_now = current
        changes = constant_changes({t: c["ten_yr"] for t, c in comparators.items()},
                                   {t: v for t, v in new_ten.items() if t in comparators})
        changes += constant_changes(treasury_now, new_treasury)
        print("\nChanged versus the script's current constants:")
        if not changes:
            print("  (none)")
        for name, old, new in changes:
            print(f"  {name:<6} {old} -> {new}")
    print("\nStill manual: NCREIF NPI (IREI) and Preqin (CAIS). Then follow steps 5-6 "
          "of references/data/README.md.")
    return 0


def _self_check():
    """Offline: exercise the math on synthetic series with known answers."""
    ok = True

    def check(label, cond, detail=""):
        nonlocal ok
        ok = ok and cond
        print(f"{'ok  ' if cond else 'FAIL'} {label}{(' - ' + detail) if detail else ''}")

    check("quarter-end before 2026-09-27", latest_quarter_end(dt.date(2026, 9, 27)) == dt.date(2026, 6, 30))
    check("quarter-end before 2026-01-15", latest_quarter_end(dt.date(2026, 1, 15)) == dt.date(2025, 12, 31))

    # 11 years of weekday closes growing exactly 10%/yr -> 10% annualized, zero drop.
    start, days = dt.date(2015, 6, 30), []
    d = start
    while d <= dt.date(2026, 6, 30):
        if d.weekday() < 5:
            days.append((d, 1.10 ** ((d - start).days / 365.25)))
        d += dt.timedelta(days=1)
    end = dt.date(2026, 6, 30)
    r10 = annualized_return(days, end, 10)
    check("10yr return on a 10%/yr series", abs(r10 - 10.0) < 0.05, f"{r10:.3f}%")
    check("no drop on a rising series", worst_drop(days, end)[0] == 0.0)
    check("too-short series returns None", annualized_return(days[-300:], end, 5) is None)

    # A 50% fall and recovery -> worst drop -50% at the trough.
    crash = [(dt.date(2020, 1, 1), 100.0), (dt.date(2020, 2, 1), 50.0), (dt.date(2020, 3, 1), 120.0)]
    drop, trough = worst_drop(crash, dt.date(2020, 12, 31))
    check("worst drop -50% at the trough", abs(drop + 50.0) < 1e-9 and trough == dt.date(2020, 2, 1), f"{drop:.1f}%")

    rows = [{"observation_date": "2026-09-23", "DGS3MO": "4.19", "DGS2": "4.85", "DGS10": "5.11"},
            {"observation_date": "2026-09-24", "DGS3MO": "4.24", "DGS2": "", "DGS10": "5.18"}]
    fred = latest_fred_values(rows, dt.date(2026, 9, 30))
    check("FRED skips blank closes", fred["2yr"] == (dt.date(2026, 9, 23), 4.85) and fred["10yr"][1] == 5.18)

    check("constant diff ignores sub-cent noise",
          constant_changes({"VNQ": 4.92}, {"VNQ": 4.9201}) == [] and
          constant_changes({"VNQ": 4.92}, {"VNQ": 5.10}) == [("VNQ", 4.92, 5.10)])

    print("PASS" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
