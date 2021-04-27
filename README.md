# Sudoku Solver
Yet another tool for automatic [sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku) solving. Works with [basic puzzle rules](https://www.learn-sudoku.com/sudoku-rules.html). 

## Pre-requisites
- [Python 3.9 +](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Setup
```
pip install -r requirements.txt
```

## Usage
Encode sudoku puzzle to text file (see [format requirements](#sudoku-file-format-requirements)) and pass it to the script: 
```
python src/solver.py path/to/sudoku-file
```
The script attempts to solve it and (if task seems valid) writes the solution to `path/to/sudoku-file-solution`.

*WARNING: Work on algorithms are in progress. Might not crack hard puzzles.*

## Sudoku File Format Requirements

_Sudoku file is a text file designed to save Sudoku tasks and solutions._

1. File encoding: UTF-8.
1. The file must contain 9 lines.
1. Each string must include 9 digits or spaces. *Other characters* are allowed and ignored. Lines of *other characters* are allowed and ignored.

***Example of a valid Sudoku file:***

```
*************
*123*456*789*
*   *456*789*
*123*456*   *
*************
*123*   *789*
*   *   *   *
*1 4*56 * 9 *
*************
 22*456*78 
*1  *   *  9*
*123*456*789*
*************
```

## Run tests (from root directory)
```
python -m pytest -v
```

## Status
Work in progress.

## Contributors and Contacts
- [@KalinovSergey](https://github.com/KalinovSergey)
- [@JanPyton](https://github.com/JanPyton)

_Lead maintainer:_ [@balex89](https://github.com/balex89) ([balex89@gmail.com](mailto:balex89@gmail.com)). Feel free to contact!
