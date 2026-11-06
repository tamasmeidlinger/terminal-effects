"""Run a selected terminal text effect."""

import argparse

from ocsi_head import main as run_ocsi_head


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a terminal text effect.")
    parser.add_argument(
        "-ocsihead",
        action="store_true",
        help="run the OCSI head laser effect",
    )
    args = parser.parse_args()

    if args.ocsihead:
        run_ocsi_head()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
