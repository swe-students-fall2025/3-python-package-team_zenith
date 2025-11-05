# Pylloween [![CICD](https://github.com/swe-students-fall2025/3-python-package-team_zenith/actions/workflows/release.yaml/badge.svg)](https://github.com/swe-students-fall2025/3-python-package-team_zenith/actions/workflows/release.yaml)

<p align="center">
  <img src="https://raw.githubusercontent.com/swe-students-fall2025/3-python-package-team_zenith/pipfile-experiment/images/pylloween.png" alt="Pylloween Logo" width="250">
</p>

Pylloween is a simple Python package that brings Halloween fun to your terminal.  
It generates ASCII ghosts, short horror stories, and movie ideas while demonstrating modular design, testing, and CI/CD workflows. The link to the package's page on the PyPI website: https://test.pypi.org/project/pylloween/

## Teammates:

Harrison Gao (https://github.com/HTK-G)

Leo Li (https://github.com/LiShangcheng)

Evelynn Mak (https://github.com/evemak)

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

```
                                    ;::;;::;,
                                    ;::;;::;;,
                                   ;;:::;;::;;,
                   .vnmmnv%vnmnv%,.;;;:::;;::;;,  .,vnmnv%vnmnv,
                vnmmmnv%vnmmmnv%vnmmnv%;;;;;;;%nmmmnv%vnmmnv%vnmmnv
              vnmmnv%vnmmmmmnv%vnmmmmmnv%;:;%nmmmmmmnv%vnmmmnv%vnmmmnv
             vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmnv%vnmmmnv%vnmmmnv
            vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmmmnv%vnmmmnv%vnmmmnv
           vnmmnv%vnmmmmmnv%vnmm;mmmmmmnv%vnmmmmmmmm;mmnv%vnmmmnv%vnmmmnv,
          vnmmnv%vnmmmmmnv%vnmm;' mmmmmnv%vnmmmmmmm;' mmnv%vnmmmnv%vnmmmnv
          vnmmnv%vnmmmmmnv%vn;;    mmmmnv%vnmmmmmm;;    nv%vnmmmmnv%vnmmmnv
         vnmmnv%vnmmmmmmnv%v;;      mmmnv%vnmmmmm;;      v%vnmmmmmnv%vnmmmnv
         vnmmnv%vnmmmmmmnv%vnmmmmmmmmm;;       mmmmmmmmmnv%vnmmmmmmnv%vnmmmnv
         vnmmnv%vnmmmmmmnv%vnmmmmmmmmmm;;     mmmmmmmmmmnv%vnmmmmmmnv%vnmmmnv
         vnmmnv%vnmmmmm nv%vnmmmmmmmmmmnv;, mmmmmmmmmmmmnv%vn;mmmmmnv%vnmmmnv
         vnmmnv%vnmmmmm  nv%vnmmmmmmmmmnv%;nmmmmmmmmmmmnv%vn; mmmmmnv%vnmmmnv
         `vnmmnv%vnmmmm,  v%vnmmmmmmmmmmnv%vnmmmmmmmmmmnv%v;  mmmmnv%vnnmmnv'
          vnmmnv%vnmmmm;,   %vnmmmmmmmmmnv%vnmmmmmmmmmnv%;'   mmmnv%vnmmmmnv
           vnmmnv%vnmmmm;;,   nmmm;'              mmmm;;'    mmmnv%vnmmmmnv'
           `vnmmnv%vnmmmmm;;,.         mmnv%v;,            mmmmnv%vnmmmmnv'
            `vnmmnv%vnmmmmmmnv%vnmmmmmmmmnv%vnmmmmmmnv%vnmmmmmnv%vnmmmmnv'
              `vnmvn%vnmmmmmmnv%vnmmmmmmmnv%vnmmmmmnv%vnmmmmmnv%vnmmmnv'
                  `vn%vnmmmmmmn%:%vnmnmmmmnv%vnmmmnv%:%vnmmnv%vnmnv'

```

| Function                         | Description                                                     | Example                           |
| -------------------------------- | --------------------------------------------------------------- | --------------------------------- |
| `draw_ghost()`                   | Prints a random ASCII ghost                                     | `plw.draw_ghost()`                |
| `draw_pumpkin()`                 | Prints a random ASCII pumpkin                                   | `plw.draw_pumpkin()`              |
| `ghost_say(message)`             | Prints a ghost with a message bubble                            | `plw.ghost_say("HTK-G!")`         |
| `ghost_story(length)`            | Displays a ghost telling a story (`short`, `medium`, `long`)    | `plw.ghost_story("short")`        |
| `ghost_idea(genre)`              | Ghost recommends a movie (`horror`, `comedy`, `cartoon`, `all`) | `plw.ghost_idea("horror")`        |
| `get_horror(length)`             | Returns a story string based on length                          | `plw.get_horror("medium")`        |
| `get_movie_idea(genre)`          | Returns a random movie title                                    | `plw.get_movie_idea("comedy")`    |
| `trick_or_treat(n, bag, seed)`   | Returns sampled candies and counts`(picks, counts)`             | `plw.trick_or_treat(10, seed=42)` |
---

## Installation

From TestPyPI:

```bash
pip install -i https://test.pypi.org/simple/ pylloween
```

<!--
From PyPI (after release):

```bash
pip install pylloween
``` -->

---

## Usage

### Import in Python

```python
import pylloween as plw

plw.ghost_say("Hello world!")
plw.ghost_story("medium")
print(plw.get_movie_idea("cartoon"))

plw.draw_pumpkin()

picks, counts = plw.trick_or_treat(n=12, seed=2025)
print(picks)
print(counts)
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
│       ├── horrors.py
|       ├── pumpkin.py
|       └── treats.py
├── tests/
│   ├── test_ghosts.py
│   ├── test_horrors.py
|   ├── test_pumpkin.py
|   └── test_treats.py
├── pyproject.toml
└── .github/
    └── workflows/
        ├── build.yaml
```

---

## License

GNU v3 License. See `LICENSE` for details.
