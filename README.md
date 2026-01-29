# M+ Repository Template
A versatile [Copier](https://copier.readthedocs.io/en/stable/) template for bootstrapping new projects at M+.

## Features
- Base Python App
  - Tools: Ruff, Pylint
- JavaScript/TypeScript
  - Tools: Biome
- Odoo Modules
  - Based on Python stack
- Jinja2 Templates
  - Tools: j2lint

## Prerequisites
Before using this template, ensure you have Copier and pre-commit installed.
```bash
pipx install copier
pipx install pre-commit
```
or, use another tools such as `uv`, `conda`, or any-else.

## Usage
### Generate a New Project
To create a new project using this template, run:
```bash
copier copy --trust gh:mplus-oss/repo-template path/to/destination
```
