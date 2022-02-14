# Sudoku Solver
Yet another tool for automatic [sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku) solving. Works with [basic puzzle rules](https://www.learn-sudoku.com/sudoku-rules.html).

See [Sudoku Solver Fronted project](https://github.com/balex89/sudoku-solver-frontend) for user web interface module.

## Prerequisites
- [Docker 20.10+](https://docs.docker.com/engine/install/) (_for amd64 linux platform only_)

or

- [Python 3.9 +](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Docker setup and run
Pull the latest build available:
```shell
docker pull kalinbob/sudoku-solver:latest
```
Or use one of stable [release versions](https://hub.docker.com/repository/docker/kalinbob/sudoku-solver) (see [release notes](https://github.com/balex89/sudoku-solver-frontend/releases) for details).

Run pulled `<VERSION>` on `<PORT>` of your choice:
```shell
docker run --name=sudoku-solver -d -p <PORT>:5000 kalinbob/sudoku-solver:<VERSION>
```
Add this option for writing logs to`<DIRECTORY>` on the host:
```shell
-v <DIRECTORY>:/app/logs
```


## Classic setup, test and run
### Setup
```commandline
pip install -r requirements.txt
```

### Run tests (from root directory)
```commandline
python -m pytest -v
```

### Run web-server
On Windows (e.g. on port 5000):
```shell
cd src/
set FLASK_APP=app.main
python -m flask run -h 0.0.0.0 -p 5000
```

## Server usage
Using `curl` (on Windows 10 works with v.1803 +):
### Check health
```shell
curl -X GET http://<host>:<port>/v1/health
```

Example: 
```shell
curl -X GET http://localhost:5000/v1/health
```

### Get sudoku solution
```shell
curl -X POST http://<host>:<port>/v1/solve -H "Content-type:application/json" -d "{\"grid\": <grid>}"
```
Here `<grid>` is a 9x9 nested array.

Example:
```shell
curl -X POST http://localhost:5000/v1/solve -H "Content-type:application/json" -d "{\"grid\": [[2, 4, 7, null, 9, 1, null, 6, 8],[1, null, 5, 7, 6, null, 3, null, null],[8, 6, null, 4, null, null, null, null, 7],[9, null, null, 2, null, 6, null, null, null],[null, null, null, 9, 4, 7, 6, 8, null],[6, null, 4, null, 5, null, null, 1, 9],[7, null, null, null, 3, null, 9, 2, null],[4, null, 9, 6, null, null, null, null, null],[null, null, null, null, null, null, 4, null, 3]]}"
```

Normal response data is JSON:
```
{"status": "ok", "grid": <UPDATED_GRID>}
```

### Get (pretty hard) Sudoku puzzle
```shell
curl -X GET http://<host>:<port>/v1/get_task -H "Accept:application/json"
```

Example:
```shell
curl -X GET http://localhost:5000/v1/get_task -H "Accept:application/json"
```

Normal response data is JSON:
```
{"status": "ok", "grid": <PUZZLE_GRID>}
```

## Local usage (via a file)
Encode sudoku puzzle to text file (see [format requirements](#sudoku-file-format-requirements)) and pass it to the script: 
```shell
python src/solver.py path/to/sudoku-file
```
The script attempts to solve it and (if task seems valid) writes the solution to `path/to/sudoku-file-solution`.

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
Development is in progress. 

## Contributors and Contacts
- [@KalinovSergey](https://github.com/KalinovSergey)
- [@JanPyton](https://github.com/JanPyton)

_Lead maintainer:_ [@balex89](https://github.com/balex89) 

Feel free to contact us: team@kalinbob.com
