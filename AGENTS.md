# Repository Guidelines

## Project Structure & Module Organization
This package uses the conventional `src/` layout: core modules live in `src/path_extract/`, where `cli.py` defines the Cyclopts-powered entry point exposed as the `pathex` script and `__init__.py` wires it for packaging. Documentation drafts sit alongside the code in `README.md` and `main.md`, and dependency state is pinned by `uv.lock`. Add new modules under `src/path_extract/` and keep exploratory notebooks or large assets outside the package tree.

## Build, Test, and Development Commands
- `uv sync` — create or update the local environment exactly as described by `pyproject.toml` and `uv.lock`.
- `uv run pathex --help` — exercise the CLI wiring; extend subcommands here when you add new features.
- `uv run python -m pytest` — execute the test suite (add `pytest` to the project’s optional dev dependencies before running if it is not yet installed).

## Coding Style & Naming Conventions
Target Python 3.13 features, keep 4-space indentation, and follow PEP 8 conventions for spacing and imports. Modules and functions should be lowercase `snake_case`; classes stay in `PascalCase`, and CLI command names should remain short and action-oriented (for example, `pathex extract`). Prefer expressive type hints and docstrings that clarify inputs, outputs, and side effects.

## Testing Guidelines
Place tests under a top-level `tests/` package mirroring the source layout (e.g., `tests/test_cli.py`). Write cases with `pytest`, name files and functions `test_*`, and cover new code paths, especially Cyclopts command handlers and data transformation logic. Aim for high branch coverage and include regression tests whenever you fix a bug; failing cases should accompany the fix in the same pull request.

## Commit & Pull Request Guidelines
Follow the existing Conventional Commit style observed in history (`feat:`, `chore:`, etc.), keeping summaries under 72 characters and scoping changes per commit. Pull requests should describe the motivation, outline significant code paths touched, list manual or automated checks performed (reference commands from the build section), and link related issues. Request at least one review before merging and update documentation or examples together with functional changes.
