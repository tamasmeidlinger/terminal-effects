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
        "-ocsihead",
        action="store_true",
        help="run the OCSI head laser effect",
    )
    parser.add_argument(
        "-ocsibody",
        action="store_true",
        help="run the OCSI body burn effect",
    )
    parser.add_argument(
        "-mucihead",
        action="store_true",
        help="run the MUCI head laser effect",
    )
    parser.add_argument(
        "-mucibody",
        action="store_true",
        help="run the MUCI body burn effect",
    )
    parser.add_argument(
        "-muciocsihead",
        action="store_true",
        help="run the MUCI-OCSI head fireworks effect",
    )
    args = parser.parse_args()

    if args.muciocsihead:
        run_muci_ocsi_head()
    elif args.mucihead:
        run_muci_head()
    elif args.mucibody:
        run_muci_body()
    elif args.ocsihead or not args.ocsibody:
        run_ocsi_head()
    elif args.ocsibody:
        run_ocsi_body()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
