# Everyone should be able to configure ArduPilot for their vehicles

<!--
SPDX-FileCopyrightText: 2024 Amilcar do Carmo Lucas <amilcar.lucas@iav.de>

SPDX-License-Identifier: GPL-3.0-or-later
-->

| Lint | Quality | Test | Deploy | Maintain |
| ---- | ------- | ---- | ------ | -------- |
| [![Pylint](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/pylint.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/pylint.yml) | [![Codacy Badge](https://app.codacy.com/project/badge/Grade/720794ed54014c58b9eaf7a097a4e98e)](https://app.codacy.com/gh/amilcarlucas/MethodicConfigurator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) | [![Python unit-tests](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/unit-tests.yml) | [![pages-build-deployment](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/pages/pages-build-deployment) | [![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/ArduPilot/MethodicConfigurator.svg)](http://isitmaintained.com/project/ArduPilot/MethodicConfigurator) |
| [![test Python cleanliness](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/ruff.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/ruff.yml) | [![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9101/badge)](https://www.bestpractices.dev/projects/9101) | [![Pytest unittests](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/unittests.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/unittests.yml) | [![Upload MethodicConfigurator Package](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/python-publish.yml) | [![Percentage of issues still open](http://isitmaintained.com/badge/open/ArduPilot/MethodicConfigurator.svg)](http://isitmaintained.com/project/ArduPilot/MethodicConfigurator) |
| [![mypy](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/mypy.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/mypy.yml) | [![Known Vulnerabilities](https://snyk.io/test/github/amilcarlucas/MethodicConfigurator/badge.svg)](https://app.snyk.io/org/amilcarlucas/project/c8fd6e29-715b-4949-b828-64eff84f5fe1) | [![codecov](https://codecov.io/github/amilcarlucas/MethodicConfigurator/graph/badge.svg?token=76P928EOL2)](https://codecov.io/github/amilcarlucas/MethodicConfigurator) | [![Windows Build](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/windows_build.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/windows_build.yml) | |
| [![markdown](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/markdown-lint.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/markdown-lint.yml) | [![Code Climate](https://codeclimate.com/github/amilcarlucas/MethodicConfigurator.png)](https://codeclimate.com/github/amilcarlucas/MethodicConfigurator) | [![Coverity Scan Build Status](https://scan.coverity.com/projects/30346/badge.svg)](https://scan.coverity.com/projects/ardupilot-methodic-configurator) | | |
| [![md-link-check](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/markdown-link-check.yml/badge.svg)](https://github.com/ArduPilot/MethodicConfigurator/actions/workflows/markdown-link-check.yml) | | | | |

Amilcar Lucas's ArduPilot Methodic Configurator is a software that semi-automates a
[clear, proven and safe configuration sequence for ArduCopter drones](https://ardupilot.github.io/MethodicConfigurator/TUNING_GUIDE_ArduCopter).

- **clear**: the sequence is linear, executed one step at the time with no hidden complex dependencies
- **proven**: the software has been used by hundreds of ArduPilot developers and users. From beginners to advanced. On big and small vehicles.
- **safe**: the sequence reduces trial-and-error and aims at reducing the amount of flights required to configure the vehicle

![When to use ArduPilot Methodic Configurator](https://github.com/ArduPilot/MethodicConfigurator/blob/master/images/when_to_use_amc.png?raw=true)

It provides a graphical user interface (GUI) for managing and visualizing ArduPilot parameters, parameter files and documentation.

![Application Screenshot](https://github.com/ArduPilot/MethodicConfigurator/blob/master/images/App_screenshot1.png?raw=true)

We are working on extending it to [ArduPlane](https://ardupilot.github.io/MethodicConfigurator/TUNING_GUIDE_ArduPlane),
[Heli](https://ardupilot.github.io/MethodicConfigurator/TUNING_GUIDE_Heli) and
[Rover](https://ardupilot.github.io/MethodicConfigurator/TUNING_GUIDE_Rover) vehicles.
But for those it is still very incomplete.

## Usage

There is a [Quick-start guide](https://ardupilot.github.io/MethodicConfigurator/QUICKSTART.html) and a more detailed [Usermanual](https://ardupilot.github.io/MethodicConfigurator/USERMANUAL.html)

## MS Windows Installation

Download the [latest MethodicConfiguratorSetup-x.x.x.exe installer file](https://github.com/ArduPilot/MethodicConfigurator/releases/tag/latest).

## Linux Installation

### Older distros without venv

Install [python pip](https://pypi.org/project/pip/). Then do:

```bash
pip install -U ardupilot_methodic_configurator
```

To run it do:

```bash
ardupilot_methodic_configurator
```

### Newer distros with venv

```bash
python -m venv .ardupilot_methodic_configurator_venv
source .ardupilot_methodic_configurator_venv/bin/activate
python -m pip install --upgrade pip
pip install ardupilot_methodic_configurator
```

To run it do:

```bash
source .ardupilot_methodic_configurator_venv/bin/activate
ardupilot_methodic_configurator
```

## MacOS Installation

Install [git](https://git-scm.com/) and [python](https://www.python.org/downloads/). Then do:

```bash
git clone https://github.com/ArduPilot/MethodicConfigurator.git
cd MethodicConfigurator
./install_macos.sh
```

## Support and Contributing

Please feel free to submit [issues](https://github.com/ArduPilot/MethodicConfigurator/issues) or
[pull requests](https://github.com/ArduPilot/MethodicConfigurator/pulls).
More information is available on the [contributing and support](https://github.com/ArduPilot/MethodicConfigurator/blob/master/CONTRIBUTING.md) page.

## Software architecture

To meet the [Software requirements](https://ardupilot.github.io/MethodicConfigurator/ARCHITECTURE.html#software-requirements) a
[software architecture](https://ardupilot.github.io/MethodicConfigurator/ARCHITECTURE.html#the-software-architecture) was designed and implemented.

## Code of conduct

To use and develop this software you must obey the [ArduPilot Methodic Configurator Code of Conduct](https://github.com/ArduPilot/MethodicConfigurator/blob/master/CODE_OF_CONDUCT.md).

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/ArduPilot/MethodicConfigurator/blob/master/LICENSE.md).
It builds upon other [open-source software packages](https://ardupilot.github.io/MethodicConfigurator/credits/CREDITS.html)
