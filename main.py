"""Run a selected terminal text effect."""

import argparse

from effects.ocsi_head import main as run_ocsi_head
from effects.ocsi_body import main as run_ocsi_body


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a terminal text effect.")
    parser.add_argument(
        "-ocsihead",
        action="store_true",
        help="run the OCSI head laser effect",
    )
    parser.add_argument(
        "-ocsibody",
        action="store_true",
        help="run the OCSI body burn effect",
    )
    args = parser.parse_args()

    if args.ocsihead:
        run_ocsi_head()
    elif args.ocsibody:
        run_ocsi_body()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
