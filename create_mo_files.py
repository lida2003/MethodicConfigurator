#!/usr/bin/env python3

"""
Create .mo files from the .po files.

This file is part of Ardupilot methodic configurator. https://github.com/ArduPilot/MethodicConfigurator

SPDX-FileCopyrightText: 2024 Amilcar do Carmo Lucas <amilcar.lucas@iav.de>

SPDX-License-Identifier: GPL-3.0-or-later
"""

import os
import subprocess


def process_locale_directory(locale_dir: str) -> None:
    """Process a single locale directory."""
    po_file = os.path.join(locale_dir, "ardupilot_methodic_configurator.po")
    mo_file = os.path.join(locale_dir, "ardupilot_methodic_configurator.mo")

    try:
        # Run msgfmt command
        cmd = ["msgfmt", "-o", mo_file, po_file]
        subprocess.run(cmd, check=True, capture_output=True, text=True)  # noqa: S603
        print(f"Successfully processed {locale_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {locale_dir}: {e}")


def main() -> None:
    # Walk through all locale directories
    for root, dirs, _files in os.walk(os.path.join("ardupilot_methodic_configurator", "locale")):
        if "LC_MESSAGES" in dirs:
            locale_dir = os.path.join(root, "LC_MESSAGES")
            process_locale_directory(locale_dir)


if __name__ == "__main__":
    main()
