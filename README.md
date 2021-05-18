# Sudoku Solver
Yet another tool for automatic [sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku) solving. Works with [basic puzzle rules](https://www.learn-sudoku.com/sudoku-rules.html). 

## Pre-requisites
- [Python 3.9 +](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Setup
```commandline
pip install -r requirements.txt
```

## Run tests (from root directory)
```commandline
python -m pytest -v
```

## Run web-server
On Windows:
```
cd src/
set FLASK_APP=app.main
python -m flask run -h 0.0.0.0 -p 5000
```

## Server usage
Using `curl` (on Windows 10 works with v.1803 +):
### Check health
```commandline
curl -X GET http://localhost:5000/health
```
### Get sudoku solution
```
curl -X POST http://localhost:5000/solve -H "Content-type:application/json" -d "{\"grid\": <GRID>>}"
```
Here `<GRID>` is a 9x9 nested array like this:
```json
[
  [2, 4, 7, null, 9, 1, null, 6, 8],
  [1, null, 5, 7, 6, null, 3, null, null],
  [8, 6, null, 4, null, null, null, null, 7],
  [9, null, null, 2, null, 6, null, null, null],
  [null, null, null, 9, 4, 7, 6, 8, null],
  [6, null, 4, null, 5, null, null, 1, 9],
  [7, null, null, null, 3, null, 9, 2, null],
  [4, null, 9, 6, null, null, null, null, null],
  [null, null, null, null, null, null, 4, null, 3]
]
```
Normal response is JSON:
```
{"status": "ok", "grid": <UPDATED_GRID>}
```

## Local usage (via a file)
Encode sudoku puzzle to text file (see [format requirements](#sudoku-file-format-requirements)) and pass it to the script: 
```commandline
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
```text
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


## Status
Work in progress.

## Contributors and Contacts
- [@KalinovSergey](https://github.com/KalinovSergey)
- [@JanPyton](https://github.com/JanPyton)

_Lead maintainer:_ [@balex89](https://github.com/balex89) ([balex89@gmail.com](mailto:balex89@gmail.com)). Feel free to contact!
