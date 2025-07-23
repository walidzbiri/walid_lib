# walid-lib

[![Continuous Delivery](https://github.com/walidzbiri/walid_lib/actions/workflows/release.yml/badge.svg)](https://github.com/walidzbiri/walid_lib/actions/workflows/release.yml)

A demonstration package for learning and practicing Python package lifecycle management using semantic versioning, conventional commits, and modern dependency management with uv.

## Overview

This package serves as a training ground for understanding how to properly manage the lifecycle of a Python package using:

- [Python Semantic Release](https://python-semantic-release.readthedocs.io/) for automated versioning
- [Conventional Commits](https://www.conventionalcommits.org/) for standardized commit messages
- [uv](https://github.com/astral-sh/uv) for ultra-fast dependency management
- GitHub Actions for continuous integration and delivery

## Features

- Automated version management based on commit messages
- Release candidate (RC) versioning for non-main branches
- Proper package structure following Python best practices
- Modern dependency management with uv
- GitHub Actions workflow for automated releases


## Conventional Commits

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages. This enables automatic versioning and changelog generation.

Commit message format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Examples:

```
feat: add new API endpoint
fix: resolve null pointer exception
feat!: redesign user interface
```

## Semantic Versioning

This package follows [Semantic Versioning](https://semver.org/) (SemVer) principles:

- MAJOR version for incompatible API changes
- MINOR version for backward-compatible functionality additions
- PATCH version for backward-compatible bug fixes

This project uses [uv](https://github.com/astral-sh/uv), an extremely fast Python package manager written in Rust. uv provides significant performance improvements over traditional tools:

- 10-100x faster than pip for package installation
- Efficient dependency resolution
- Global caching for dependency deduplication
- Compatible with existing Python packaging standards

The project's semantic release process uses uv for building and dependency management, as configured in the `pyproject.toml` file.

### Release Process

Releases are handled automatically by the GitHub Actions workflow in `.github/workflows/release.yml`. When commits are pushed to any branch:

1. For the `main` branch:
   - Semantic Release analyzes commit messages
   - Updates version in `pyproject.toml`
   - Creates a new tag
   - Generates/updates the changelog
   - Creates a GitHub release

2. For other branches:
   - Creates release candidates with the `-rc` suffix
   - Appends build metadata when appropriate

## License

MIT

## Author

- [walidzbiri](https://github.com/walidzbiri) - walid.zbiri@uit.ac.ma

## TODO:
- Add linting for commit messages.
- Add ruff linter and formatter
- Add static type checking using mypy
- Add tests for the package.
- Explain the lifecycle of versions