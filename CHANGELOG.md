# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **Dropped Python 3.10** (end of life October 2026). Wiggle now requires
  Python 3.11 or newer.
- Packaging metadata uses an SPDX license expression (`license = "MIT"`)
  instead of the deprecated table and classifier form. Building now requires
  `setuptools>=77`.
- Added project URLs (homepage, repository, issues, changelog) to the package
  metadata.
- Refreshed the development lockfile (`uv.lock`) and moved it to public PyPI;
  it previously referenced an internal registry. CI now installs with
  `uv sync --locked`, so a stale lockfile fails the build.
- Updated GitHub Actions (`checkout` v7, `setup-python` v7, `setup-uv` v10.3.0)
  and the pre-commit Ruff hook (v0.17.0).

### Added

- Python 3.14 support: trove classifier and CI test matrix entry.
- Dependabot configuration for the `uv` and `github-actions` ecosystems.

### Security

- Development lockfile now resolves Pillow 12.3.0 and virtualenv 21.14.5,
  closing all open Dependabot alerts. These only affected the development
  environment; the package itself does not pin either dependency.

## [0.1.2] - 2026-03-07

### Changed

- Modernized the repository: type hints, Ruff linting and formatting, and
  pre-commit hooks.

Earlier releases (0.1.0, 0.1.1) are listed on the
[tags page](https://github.com/lijunzh/wiggle/tags).

[Unreleased]: https://github.com/lijunzh/wiggle/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/lijunzh/wiggle/releases/tag/v0.1.2
