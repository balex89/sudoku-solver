# sudoku-solver
Solves given classic sudoku puzzle

## Run all tests
```
python -m pytest -v
```
 
##Требования к формату файла Sudoku

_Файл Sudoku - текстовый файл, предназначенный для записи задания и решений Судоку._

1. Кодировка файла: UTF-8.
1. Файл должен содержать как минимум 9 строк (**valid string**).
1. Каждая из valid string должна включать в себя 9 цифр или знаков пробела(**valid char**).  Кроме valid chars в valid string допустимы иные символы.
1. кроме 9-ти valid strings в файле допустимы иные строки, не содержащие valid char.

***Пример корректного файла Sudoku:***

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

##Sudoku File Format Requirements

_Sudoku file is a text file designed to save Sudoku tasks and solutions._

1. File encoding: UTF-8.
1. The file must contain at least 9 lines (**valid string**).
1. Each of the valid strings must include 9 digits or spaces (**validchar**). In addition to valid chars, other characters are allowed in the valid string.
1. In addition to the 9 valid strings in the file, other strings that do not contain validchar are allowed.

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
