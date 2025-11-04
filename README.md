# Pylloween

Pylloween is a light-hearted Halloween helper for your terminal. Conjure ASCII ghosts, let them whisper (or scream!) in spooky speech bubbles, and have them pick a horror story or a movie night suggestion for you.

## Features at a Glance
- `draw_ghost(style=None)` – render one of several pre-made ASCII ghosts.
- `ghost_say(message)` – wrap any text in a ghostly speech bubble.
- `ghost_story(length)` – fetch a random short, medium, or long horror story.
- `ghost_idea(genre)` – get a Halloween movie idea across horror, comedy, cartoon, or all genres.
- Command line entry point: run `pylloween` to get a story or a movie recommendation without writing code.

## Installation

```bash
pip install pylloween
```

> Not on PyPI yet? Install straight from your local checkout:
>
> ```bash
> pip install -e ".[dev]"
> ```

## Usage

### From the command line

```bash
# Hear a short ghost story
pylloween --story short

# Let a ghost pick a movie genre
pylloween --movie comedy
```

### From Python

```python
from pylloween import draw_ghost, ghost_say, ghost_story, ghost_idea

ghost_say("Welcome to the haunted terminal.")
ghost_story("medium")
ghost_idea("all")
draw_ghost(2)  # pick a specific ghost by number
```

## Development

1. Create and activate a virtual environment.
2. Install the package in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
3. Run the automated tests:
   ```bash
   pytest
   ```
4. Build distributable artifacts (wheel + sdist) when you are ready to publish:
   ```bash
   python -m build
   ```

## Continuous Integration & Publishing

The workflow defined in `.github/workflows/python-package.yml` keeps the project healthy:
- Runs the test suite on Python 3.9–3.11 for every push and pull request to `main`.
- Builds and validates the wheel and source distribution.
- Publishes to PyPI automatically when you draft and publish a GitHub release, provided the repository secret `PYPI_API_TOKEN` is set.

## Team
- Evelynn Mak (@evemak)
- Leo Li (https://github.com/LiShangcheng)
- Harrison Gao (hg2655@nyu.edu)
- Christine Jin (https://github.com/Christine-Jin)
