"""Run a selected terminal text effect."""

import argparse

from effects.ocsi_head import main as run_ocsi_head
from effects.ocsi_body import main as run_ocsi_body
from effects.muci_head import main as run_muci_head
from effects.muci_body import main as run_muci_body
from effects.muci_ocsi_head import main as run_muci_ocsi_head


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a terminal text effect.")
    parser.add_argument(
        "-oh",
        action="store_true",
        help="run the OCSI head laser effect",
    )
    parser.add_argument(
        "-ob",
        action="store_true",
        help="run the OCSI body burn effect",
    )
    parser.add_argument(
        "-mh",
        action="store_true",
        help="run the MUCI head laser effect",
    )
    parser.add_argument(
        "-mb",
        action="store_true",
        help="run the MUCI body burn effect",
    )
    parser.add_argument(
        "-moh",
        action="store_true",
        help="run the MUCI-OCSI head fireworks effect",
    )
    args = parser.parse_args()

    if args.moh:
        run_muci_ocsi_head()
    elif args.mh:
        run_muci_head()
    elif args.mb:
        run_muci_body()
    elif args.oh or not args.ob:
        run_ocsi_head()
    elif args.ob:
        run_ocsi_body()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
