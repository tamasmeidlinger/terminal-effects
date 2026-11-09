"""Run the MUCI head laser effect."""

import os
import subprocess
from pathlib import Path

from terminaltexteffects.effects.effect_laseretch import LaserEtch, LaserEtchConfig
from terminaltexteffects.engine.terminal import TerminalConfig


def main(*, centered: bool = False) -> None:
    art = (Path(__file__).parent.parent / "ascii_arts" / "muci-head.txt").read_text(encoding="utf-8").rstrip("\n")

    config = LaserEtchConfig._build_config()
    config.etch_speed = 4
    config.etch_delay = 0

    terminal_config = TerminalConfig._build_config()
    if centered:
        terminal_config.canvas_width = 0
        terminal_config.canvas_height = 0
    terminal_config.anchor_canvas = "c" if centered else "s"
    terminal_config.anchor_text = "c"
    effect = LaserEtch(art, effect_config=config, terminal_config=terminal_config)

    clear_command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(clear_command, check=False)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


if __name__ == "__main__":
    main()
