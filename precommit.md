# Precommit

## Setup

- `pip install pre-commit` (already installed in poetry env by default)
- Install the git hook scripts in `.pre-commit-config.yaml`: `pre-commit install`
- detect secrets setup
  - `detect-secrets scan > .secrets.baseline`
- auto update: `pre-commit autoupdate`

### Setup from scratch (without code already existing in this repo)

- create `.pre-commit-config.yaml`
  - populate with `pre-commit sample-config`
- plugins

  - list of some plugins

    - https://pre-commit.com/hooks.html

  - flake8: add `.flake8` file
  - black: add to `pyproject.toml`

    ```toml
    [tool.black]
    py36 = true
    include = '\.pyi?$'
    exclude = '''
    /(
    \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | \_build
    | buck-out
    | build
    | dist
    # The following are specific to Black, you probably don't want those.
    | blib2to3
    | tests/data
    )/
    '''
    ```

## Usage

- `pre-commit run --all-files`

### know issues

- out of date revs
  - auto update: `pre-commit autoupdate`
