"""Run the MUCI body burn effect."""

import os
import subprocess
from pathlib import Path

from terminaltexteffects.effects.effect_burn import Burn, BurnConfig
from terminaltexteffects.engine.terminal import TerminalConfig


def main() -> None:
    art = (Path(__file__).parent.parent / "ascii_arts" / "muci-body.txt").read_text(encoding="utf-8").rstrip("\n")

    config = BurnConfig._build_config()
    terminal_config = TerminalConfig._build_config()
    terminal_config.frame_rate = 150
    terminal_config.anchor_canvas = "s"
    terminal_config.anchor_text = "c"
    effect = Burn(art, effect_config=config, terminal_config=terminal_config)

    clear_command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(clear_command, check=False)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


if __name__ == "__main__":
    main()
