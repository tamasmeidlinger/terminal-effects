"""Etch the OCSI head in with a laser effect."""

import os
import subprocess
from pathlib import Path

from terminaltexteffects.effects.effect_laseretch import LaserEtch, LaserEtchConfig
from terminaltexteffects.engine.terminal import TerminalConfig


def main() -> None:
    art = (
        Path(__file__)
        .with_name("ocsi-head.txt")
        .read_text(encoding="utf-8")
        .rstrip("\n")
    )
    config = LaserEtchConfig._build_config()
    config.etch_speed = 4  # Etch four characters per pass instead of one.
    config.etch_delay = 0  # Don't pause between passes.
    terminal_config = TerminalConfig._build_config()
    # Center horizontally without reserving blank rows below the artwork.
    terminal_config.anchor_canvas = "s"
    terminal_config.anchor_text = "c"
    effect = LaserEtch(art, effect_config=config, terminal_config=terminal_config)

    clear_command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(clear_command, check=False)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


if __name__ == "__main__":
    main()
