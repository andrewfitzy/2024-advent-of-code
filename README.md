# 2024-advent-of-code

![Build status](https://github.com/andrewfitzy/2024-advent-of-code/actions/workflows/build-and-test-project.yml/badge.svg)

Each day, [advent of code](https://adventofcode.com/2024) presents a challenge for those of brave heart to complete.
This repo contains my answers to the 2024 version of advent of code, not all challenges have been completed. I complete
AoC to get familiar with a technology, its build tools and testing tools, it's kind of a mini-production type workflow
I follow.

In this year I chose to use the following tools:
- [Python v3.13.0](https://www.python.org). Language for this years AOC solutions.
- [Mypy v1.13.0](https://mypy.readthedocs.io/en/stable/). Typing for Python code.
- [ruff v0.8.0](https://docs.astral.sh/ruff/). Linter for python code.
- [isort v5.13.2](https://pycqa.github.io/isort/). Sorts imports in python code.
- [pytest v8.3.3](https://docs.pytest.org/en/7.4.x/). Testing framework for python code.
- [pre-commit v4.0.1](https://pre-commit.com). Used for pre commit hooks.
- [uv 0.5.4](https://docs.astral.sh/uv/). Used as the package manager in place of `pip`

All development is completed using [VS Code](https://code.visualstudio.com).

## Setup
With Python, I like to work with virtual envs, this keeps the development environments for each project separate.

First step is to install the version of python to use. I use pyenv to manage my python versions, so I install
the version I want to use with the following command:
```bash
╰─❯ pyenv install 3.13.0
````

Next I create a virtual environment for the project:
```bash
╰─❯ pyenv virtualenv 3.13.0 2024-aoc
```

Then I activate the virtual environment:
```bash
╰─❯ pyenv activate 2024-aoc
```

Install the dependencies:
```bash
╰─❯ make install
```

Finally, set up pre-commit:
```bash
╰─❯ pre-commit install
```

My environment is now setup and ready to go.

## Testing
```bash
╰─❯ make test
```

## Committing
The pre-commit hook should kick-in, when it does it will lint and prettify the code.
```bash
╰─❯ git add --all
╰─❯ git commit -a
```

## Progress
|                                                | Challenge             |                                         Task 1                                          |                                         Task 2                                          |
| :--------------------------------------------- | :-------------------- | :-------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------: |
| [Day 01](https://adventofcode.com/2024/day/1)  | Historian Hysteria    | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_01/task_01.py) | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_01/task_02.py) |
| [Day 02](https://adventofcode.com/2024/day/2)  | Red-Nosed Reports     | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_02/task_01.py) | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_02/task_02.py) |
| [Day 03](https://adventofcode.com/2024/day/3)  | Mull It Over          | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_03/task_01.py) | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_03/task_02.py) |
| [Day 04](https://adventofcode.com/2024/day/4)  | Ceres Search          | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_04/task_01.py) | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_04/task_02.py) |
| [Day 05](https://adventofcode.com/2024/day/5)  | Print Queue           | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_05/task_01.py) | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_05/task_02.py) |
| [Day 06](https://adventofcode.com/2024/day/6)  | Guard Gallivant       | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_06/task_01.py) | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_06/task_02.py) |
| [Day 07](https://adventofcode.com/2024/day/7)  | Bridge Repair         | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_07/task_01.py) | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_07/task_02.py) |
| [Day 08](https://adventofcode.com/2024/day/8)  | Resonant Collinearity | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_08/task_01.py) | [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_08/task_02.py) |
| [Day 09](https://adventofcode.com/2024/day/9)  | Disk Fragmenter       |  [🌟](https://github.com/andrewfitzy/2024-advent-of-code/blob/main/src/day_09/task_01.py) |                                                                                         |
| [Day 10](https://adventofcode.com/2024/day/10) | Hoof It               |                                                                                         |                                                                                         |
| [Day 11](https://adventofcode.com/2024/day/11) | Plutonian Pebbles     |                                                                                         |                                                                                         |
| [Day 12](https://adventofcode.com/2024/day/12) | Garden Groups         |                                                                                         |                                                                                         |
| [Day 13](https://adventofcode.com/2024/day/13) |                    |                                                                                         |                                                                                         |
| [Day 14](https://adventofcode.com/2024/day/14) |                    |                                                                                         |                                                                                         |
| [Day 15](https://adventofcode.com/2024/day/15) |                    |                                                                                         |                                                                                         |
| [Day 16](https://adventofcode.com/2024/day/16) |                    |                                                                                         |                                                                                         |
| [Day 17](https://adventofcode.com/2024/day/17) |                    |                                                                                         |                                                                                         |
| [Day 18](https://adventofcode.com/2024/day/18) |                    |                                                                                         |                                                                                         |
| [Day 19](https://adventofcode.com/2024/day/19) |                    |                                                                                         |                                                                                         |
| [Day 20](https://adventofcode.com/2024/day/20) |                    |                                                                                         |                                                                                         |
| [Day 21](https://adventofcode.com/2024/day/21) |                    |                                                                                         |                                                                                         |
| [Day 22](https://adventofcode.com/2024/day/22) |                    |                                                                                         |                                                                                         |
| [Day 23](https://adventofcode.com/2024/day/23) |                    |                                                                                         |                                                                                         |
| [Day 24](https://adventofcode.com/2024/day/24) |                    |                                                                                         |                                                                                         |
| [Day 25](https://adventofcode.com/2024/day/25) |                    |                                                                                         |                                                                                         |