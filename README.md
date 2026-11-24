# Wiggle Plot for Seismic Data Section

[![PyPI version](https://img.shields.io/pypi/v/wiggle)](https://pypi.org/project/wiggle/)
![License](https://img.shields.io/pypi/l/wiggle)
![Python versions](https://img.shields.io/pypi/pyversions/wiggle)
[![CI/CD](https://github.com/lijunzh/wiggle/actions/workflows/cicd.yml/badge.svg)](https://github.com/lijunzh/wiggle/actions/workflows/cicd.yml)

## Introduction

The [wiggle](http://wiki.aapg.org/Seismic_data_display) display is a
visualization methodology for two-dimensional scalar fields on a horizontal
plane. Originally developed by the geophysical community, wiggle plots
provide visual analysis of seismic, seismological, or any other vibration
data — helping identify events through the coherent alignment of lobes that
relate to geological features and physical rock properties.

Inspired by the
[MATLAB wiggle function](https://www.mathworks.com/matlabcentral/fileexchange/38691-wiggle),
this Python package offers a similar interface for plotting seismic section
data with control over colour, amplitude, and axis orientation.

Given an *M × N* `ndarray`, `wiggle` decomposes it into *N* traces of
length *M* (column-major, vertical mode by default).

## Project status: maintenance mode

wiggle is feature-complete, and no new features are planned. It stays
maintained so that it keeps installing and working. What to expect:

- **Compatibility fixes** ship as patch releases when a new Python, NumPy or
  Matplotlib version breaks something. CI tests Python 3.11–3.14.
- **Dependencies:** wiggle sets no upper version limits, so NumPy and Matplotlib
  fixes reach you through your own `pip` or `uv` upgrade, without a new
  wiggle release. Dependabot keeps the CI and development tools current.
- **Bug reports and pull requests** are welcome. Review may be slow, and
  new features are unlikely to be merged.

## Installation

### From PyPI

```bash
pip install wiggle
```

### From source (development)

```bash
git clone https://github.com/lijunzh/wiggle.git
cd wiggle
uv sync --all-extras --dev
```

Build a distribution:

```bash
uv build
```

## Quick Start

```python
import numpy as np
from wiggle import wiggle

data = np.random.default_rng(42).standard_normal((200, 20))
ax = wiggle(data, sf=0.15)
```

## Dependencies

- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

## Development

Linting and formatting are handled by [Ruff](https://docs.astral.sh/ruff/):

```bash
uv run ruff check src tests
uv run ruff format src tests
```

Run tests:

```bash
uv run pytest
```

Pre-commit hooks are available:

```bash
uv run pre-commit install
```

## Contact

For issues, please open a
[GitHub issue](https://github.com/lijunzh/wiggle/issues) or contact
*gatechzhu@gmail.com*.
