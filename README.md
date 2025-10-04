# PathEx: Pathology Report Entity Extraction

PathEx streamlines the process of structuring pathology reports by extracting key clinical entities—diagnoses, specimen attributes, and supporting context—into consistent, analysis-ready data. The toolkit is packaged as a Cyclopts-powered command-line interface (CLI) so it can slot into existing data pipelines and automation workflows.

## Highlights
- Opinionated CLI foundation using [Cyclopts](https://github.com/jamesls/cyclopts) for ergonomic subcommand design.
- Built on modern Python 3.13 and efficient data tooling such as Polars.
- Ships with a reproducible environment managed by `uv` and a packaging-friendly `src/` layout.

## Quick Start
1. **Install prerequisites**
   - Python 3.13+
   - [`uv`](https://docs.astral.sh/uv/) package manager (`pip install uv` or download the binary)
2. **Sync the environment**
   ```bash
   uv sync
   ```
3. **Run the CLI**
   ```bash
   uv run pathex --help
   ```
   Extend `src/path_extract/cli.py` with additional commands as extractor capabilities grow.

## Project Layout
```
path-extract/
├── src/path_extract/        # Library and CLI entry points
│   ├── __init__.py          # Exposes the Cyclopts App as `pathex`
│   └── cli.py               # CLI command definitions
├── README.md                # Project overview (this document)
├── AGENTS.md                # Contributor quick-reference
├── pyproject.toml           # Project metadata and dependencies
└── uv.lock                  # Reproducible environment lockfile
```
Place new extractor modules under `src/path_extract/` and keep tests in a top-level `tests/` package that mirrors the source tree (e.g., `tests/test_cli.py`).

## Development Workflow
- **Environment**: `uv sync` installs runtime and development dependencies; rerun after updating `pyproject.toml`.
- **Testing**: Add `pytest` to the optional dev dependencies and run with `uv run python -m pytest`. Commit failing tests alongside fixes.
- **Formatting**: Follow PEP 8 with 4-space indentation and descriptive docstrings. Organize imports using `isort`/`ruff` if added.

## Contributing
Use Conventional Commits (`feat:`, `chore:`, `fix:`) for history clarity. Each pull request should outline the problem solved, summarize the approach, and list manual or automated checks performed (tests, CLI runs, etc.). Link related issues and include documentation updates whenever behavior changes.
