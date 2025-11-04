# Pylloween [![CICD](https://github.com/swe-students-fall2025/3-python-package-team_zenith/actions/workflows/release.yaml/badge.svg)](https://github.com/swe-students-fall2025/3-python-package-team_zenith/actions/workflows/release.yaml)

<p align="center">
  <img src="https://raw.githubusercontent.com/swe-students-fall2025/3-python-package-team_zenith/pipfile-experiment/images/pylloween.png" alt="Pylloween Logo" width="250">
</p>

Pylloween is a simple Python package that brings Halloween fun to your terminal.  
It generates ASCII ghosts, short horror stories, and movie ideas while demonstrating modular design, testing, and CI/CD workflows.

## Teammates:

Harrison Gao (https://github.com/HTK-G)

Leo Li (https://github.com/LiShangcheng)

Evelynn Mak (evemak)

Christine Jin (https://github.com/Christine-Jin)

---

## Introduction

Pylloween is designed as a lightweight package for practicing:

- Python package structure and modularity
- Unit testing with `pytest`
- Continuous Integration and Delivery via GitHub Actions
- PyPI publishing using `build` and `twine`

---

## Features

```
  ________________________________________________________________________
 < I'm haunting your terminal! Zelle me 50 or I'll overflow your stack. >
  ------------------------------------------------------------------------

      ⣴⣿⣿⣿⣦
    ⣰⣿⡟⢻⣿⡟⢻⣧
   ⣰⣿⣿⣇⣸⣿⣇⣸⣿
  ⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
 ⠈⠿⠿⠋⠙⢿⣿⡿⠁

```

| Function                | Description                                                     | Example                        |
| ----------------------- | --------------------------------------------------------------- | ------------------------------ |
| `draw_ghost()`          | Prints a random ASCII ghost                                     | `plw.draw_ghost()`             |
| `ghost_say(message)`    | Prints a ghost with a message bubble                            | `plw.ghost_say("HTK-G!")`      |
| `ghost_story(length)`   | Displays a ghost telling a story (`short`, `medium`, `long`)    | `plw.ghost_story("short")`     |
| `ghost_idea(genre)`     | Ghost recommends a movie (`horror`, `comedy`, `cartoon`, `all`) | `plw.ghost_idea("horror")`     |
| `get_horror(length)`    | Returns a story string based on length                          | `plw.get_horror("medium")`     |
| `get_movie_idea(genre)` | Returns a random movie title                                    | `plw.get_movie_idea("comedy")` |

---

## Installation

From TestPyPI:

```bash
pip install -i https://test.pypi.org/project/pylloween/
```

From PyPI (after release):

```bash
pip install pylloween
```

---

## Usage

### Import in Python

```python
import pylloween as plw

plw.ghost_say("Hello world!")
plw.ghost_story("medium")
print(plw.get_movie_idea("cartoon"))
```

### Run via Command Line

```bash
python -m pylloween
```

### Run via Demo Script

```bash
python src/pylloween/main.py
```

---

## Running Tests

```bash
pip install pytest
pytest -v
```

---

## CI/CD Overview

This project has a continuous integration workflow that builds and runs unit tests automatically with every push of the code to GitHub.

---

## Project Structure

```
pylloween/
├── src/
│   └── pylloween/
│       ├── __init__.py
│       ├── __main__.py
│       ├── ghosts.py
│       └── horrors.py
├── tests/
│   ├── test_ghosts.py
│   └── test_horrors.py
├── pyproject.toml
└── .github/
    └── workflows/
        ├── build.yaml
```

---

## License

GNU v3 License. See `LICENSE` for details.
