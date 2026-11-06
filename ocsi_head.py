"""Run the OCSI head laser effect."""

import os
import subprocess
from pathlib import Path

from terminaltexteffects.effects.effect_laseretch import LaserEtch, LaserEtchConfig
from terminaltexteffects.engine.terminal import TerminalConfig


def main() -> None:
    art = Path(__file__).with_name("ocsi-head.txt").read_text(encoding="utf-8").rstrip("\n")

    config = LaserEtchConfig._build_config()
    config.etch_speed = 4
    config.etch_delay = 0

    terminal_config = TerminalConfig._build_config()
    terminal_config.anchor_canvas = "s"
    terminal_config.anchor_text = "c"
    effect = LaserEtch(art, effect_config=config, terminal_config=terminal_config)

    clear_command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(clear_command, check=False)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
