"""Run every terminal effect in sequence until interrupted."""

import sys

from effects.muci_body import main as run_muci_body
from effects.muci_head import main as run_muci_head
from effects.muci_ocsi_head import main as run_muci_ocsi_head
from effects.ocsi_body import main as run_ocsi_body
from effects.ocsi_head import main as run_ocsi_head


def main() -> None:
    animations = (
        run_ocsi_head,
        run_ocsi_body,
        run_muci_head,
        run_muci_body,
        run_muci_ocsi_head,
    )

    try:
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()
        while True:
            for animation in animations:
                animation(centered=True)
                # Each effect restores the terminal cursor when it finishes.
                # Hide it again before starting the next effect.
                sys.stdout.write("\x1b[?25l")
                sys.stdout.flush()
    except KeyboardInterrupt:
        print("\nAnimation loop stopped.")
    finally:
        sys.stdout.write("\x1b[?25h")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
