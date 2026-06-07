#!/usr/bin/env python3
"""
Mossarium - A constitutional system for AI-maintained software projects
"""

import argparse

from . import init
from . import check
from . import brief
from . import preflight
from . import audit
from . import refresh


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Mossarium - Constitutional system for AI-maintained software projects"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init
    subparsers.add_parser("init", help="Initialize project with constitutional files")

    # check
    subparsers.add_parser("check", help="Check project compliance with constitutional guidelines")

    # brief
    subparsers.add_parser("brief", help="Output a short AI project brief before editing")

    # preflight
    subparsers.add_parser("preflight", help="Check if the repository is ready for AI-assisted modification")

    # audit
    subparsers.add_parser("audit", help="Check whether a repository is ready for AI inheritance")

    # refresh
    refresh_parser = subparsers.add_parser("refresh", help="Refresh AI Context Map from current repository state")
    refresh_parser.add_argument("--check", action="store_true",
                                help="Only check whether context is stale, do not write")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "init":
        init.init_project()
    elif args.command == "check":
        check.check_compliance()
    elif args.command == "brief":
        brief.brief_project()
    elif args.command == "preflight":
        preflight.preflight()
    elif args.command == "audit":
        audit.audit()
    elif args.command == "refresh":
        if args.check:
            refresh.check_refresh()
        else:
            refresh.refresh_project()


if __name__ == "__main__":
    main()
