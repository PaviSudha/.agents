#!/usr/bin/env python3
"""
LaTeX Linter: Combines chktex (style) + lacheck (structure) into one report.
Usage:
    python latex_linter.py --file /path/to/file.tex
    python latex_linter.py --dir /path/to/project/
"""

import subprocess
import sys
import os
import argparse
import glob


def run_chktex(filepath):
    """Run chktex and return parsed warnings."""
    try:
        result = subprocess.run(
            ["chktex", "-q", "-v0", filepath],
            capture_output=True, text=True, check=False
        )
        issues = []
        for line in result.stdout.strip().split("\n"):
            if line.strip():
                issues.append(("STYLE", line.strip()))
        # Also parse stderr (chktex outputs warnings there)
        for line in result.stderr.strip().split("\n"):
            if line.strip() and ("Warning" in line or "Error" in line):
                issues.append(("STYLE", line.strip()))
        return issues
    except FileNotFoundError:
        print("Error: chktex not found. Install with: sudo pacman -S texlive-binextra")
        return []


def run_lacheck(filepath):
    """Run lacheck and return parsed warnings."""
    try:
        result = subprocess.run(
            ["lacheck", filepath],
            capture_output=True, text=True, check=False
        )
        issues = []
        for line in result.stdout.strip().split("\n"):
            if line.strip():
                issues.append(("STRUCTURE", line.strip()))
        return issues
    except FileNotFoundError:
        print("Error: lacheck not found. Install with: sudo pacman -S texlive-binextra")
        return []


def lint_file(filepath):
    """Run both linters on a single file."""
    if not filepath.endswith(".tex"):
        return []
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        return []

    issues = []
    issues.extend(run_chktex(filepath))
    issues.extend(run_lacheck(filepath))
    return issues


def lint_directory(dirpath):
    """Run both linters on all .tex files in directory."""
    all_issues = {}
    tex_files = glob.glob(os.path.join(dirpath, "**/*.tex"), recursive=True)

    if not tex_files:
        print(f"No .tex files found in {dirpath}")
        return all_issues

    for f in sorted(tex_files):
        file_issues = lint_file(f)
        if file_issues:
            all_issues[f] = file_issues

    return all_issues


def main():
    parser = argparse.ArgumentParser(description="LaTeX Linter (chktex + lacheck)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Single .tex file to lint")
    group.add_argument("--dir", help="Directory to lint (all .tex files)")
    args = parser.parse_args()

    if args.file:
        issues = lint_file(args.file)
        if not issues:
            print("✓ No issues found.")
            return

        print(f"Found {len(issues)} issues in {os.path.basename(args.file)}:\n")
        for category, msg in issues:
            print(f"  [{category}] {msg}")

    elif args.dir:
        all_issues = lint_directory(args.dir)
        if not all_issues:
            print("✓ No issues found across all .tex files.")
            return

        total = sum(len(v) for v in all_issues.values())
        print(f"Found {total} issues across {len(all_issues)} files:\n")
        for filepath, issues in all_issues.items():
            print(f"--- {os.path.basename(filepath)} ({len(issues)} issues) ---")
            for category, msg in issues:
                print(f"  [{category}] {msg}")
            print()


if __name__ == "__main__":
    main()
