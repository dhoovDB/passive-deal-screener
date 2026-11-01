#!/usr/bin/env python3
"""Mechanical checks on one eval iteration, run before the grader.

Checks that every cited flag and question ID exists in references 03 and 04, and that the
required notice sits on its own line directly under both the top verdict and section 10's.
Exit codes: 0 all clean, 1 a report needs the grader's attention, 2 bad input.
Stdlib only. Not part of the shipped skill.
"""
import argparse
import glob
import os
import re
import sys

NOTICE = "Screening output only, not investment advice."
FLAG = re.compile(r"\b(?:GEN|EQUITY|PREF|HML|CREDIT)-\d{2}\b")
QUESTION = re.compile(r"\bQ-[A-Z]+-\d{2}\b")


def known_ids(path, pattern):
    with open(path, encoding="utf-8") as f:
        return set(pattern.findall(f.read()))


def next_text_line(lines, start):
    """Index of the first non-blank line after start, or None."""
    for i in range(start + 1, len(lines)):
        if lines[i].strip():
            return i
    return None


def is_notice(line):
    return line.strip().strip("*_").strip() == NOTICE


def notice_follows(lines, verdict_at):
    """True if the next line after the verdict is the notice and nothing else.

    A comparison has one verdict line per deal, so walk the verdict paragraph, checking the
    line after each verdict line before treating it as more of the verdict.
    """
    if verdict_at is None:
        return False
    end = verdict_at
    while end + 1 < len(lines) and lines[end + 1].strip():
        if is_notice(lines[end + 1]):
            return True
        end += 1
    i = next_text_line(lines, end)
    return i is not None and is_notice(lines[i])


def check_report(lines):
    """Return (top_ok, section_10_ok) for the notice placement."""
    top = next((i for i, line in enumerate(lines) if line.startswith("**Verdict")), None)
    heading = next((i for i, line in enumerate(lines) if re.match(r"#+\s*10\b", line)), None)
    section_verdict = None if heading is None else next_text_line(lines, heading)
    return notice_follows(lines, top), notice_follows(lines, section_verdict)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iteration", help="folder holding the NN-*.md reports")
    parser.add_argument("--references", default="references", help="folder holding 03 and 04")
    parser.add_argument("--expected", type=int, default=13, help="number of reports required")
    args = parser.parse_args()

    reports = sorted(glob.glob(os.path.join(args.iteration, "[0-9][0-9]-*.md")))
    if len(reports) != args.expected:
        print(f"expected {args.expected} reports, found {len(reports)}")
        return 2

    flags = known_ids(os.path.join(args.references, "03-red-flag-library.md"), FLAG)
    questions = known_ids(os.path.join(args.references, "04-question-bank.md"), QUESTION)

    needs_attention = 0
    for path in reports:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        top_ok, section_ok = check_report(text.splitlines())
        bad_ids = sorted((set(FLAG.findall(text)) - flags) | (set(QUESTION.findall(text)) - questions))
        ok = top_ok and section_ok and not bad_ids
        needs_attention += not ok
        print(f"{os.path.basename(path)[:40]:40} top={top_ok!s:5} s10={section_ok!s:5} "
              f"bad_ids={bad_ids} {'ok' if ok else 'CHECK'}")
    print(f"reports needing attention: {needs_attention} of {len(reports)}")
    return 1 if needs_attention else 0


if __name__ == "__main__":
    sys.exit(main())
