"""Etch the OCSI head in with a laser effect."""

from pathlib import Path

from terminaltexteffects.effects.effect_laseretch import LaserEtch, LaserEtchConfig


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
    effect = LaserEtch(art, effect_config=config)

    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


if __name__ == "__main__":
    main()
