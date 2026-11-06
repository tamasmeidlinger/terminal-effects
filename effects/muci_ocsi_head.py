"""Run the MUCI-OCSI head fireworks effect."""

import os
import subprocess
from pathlib import Path

from terminaltexteffects.effects.effect_fireworks import Fireworks, FireworksConfig
from terminaltexteffects.engine.terminal import TerminalConfig
from terminaltexteffects.utils.graphics import Color, Gradient


def main() -> None:
    art = (Path(__file__).parent.parent / "ascii_arts" / "muci-ocsi-head.txt").read_text(encoding="utf-8").rstrip("\n")

    config = FireworksConfig._build_config()
    config.launch_delay = 15
    config.firework_colors = (
        Color("#19ECFF"),
        Color("#5598FF"),
        Color("#9955F5"),
        Color("#FF4D9B"),
        Color("#C4F5FA"),
    )
    config.final_gradient_stops = (Color("#9A4DE0"), Color("#00D5ED"), Color("#C4F5FA"))
    config.final_gradient_direction = Gradient.Direction.VERTICAL
    terminal_config = TerminalConfig._build_config()
    terminal_config.frame_rate = 150
    terminal_config.anchor_canvas = "s"
    terminal_config.anchor_text = "c"
    effect = Fireworks(art, effect_config=config, terminal_config=terminal_config)

    clear_command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(clear_command, check=False)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


if __name__ == "__main__":
    main()
