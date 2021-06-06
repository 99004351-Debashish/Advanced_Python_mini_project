# Genesis Advanced python project
* work done on this project from 2nd june to 7th june
* Author: Debashish Dash
* Ps number: 99004351
----
## Contents
* [About](#About)
* [Summary Table](#Summary_Table)
* [Folde Structure](#folder_structure)
* [Directory Tree](#Directory_Tree)
----
## About
* This mini project is an appliction that fetch data from a excel sheet and stores the fetched data in another excel sheet
* It first asks the user to enter the Ps number of which he/she wants to fetch the data.
* Then it asks the user to enter the sheet name from which sheet he/she wants to fetch data.
* Then it fetch the data from the respective sheet and prints in the screen and also writes those data to another excel sheet called Outputs.xlsx
* user also gets an **option to enter another sheet name** to fetch data or he/she can **move back if he/she wants to fetch data from a different ps number** or he/she **can exit** the code.
* **Exceptions** are **Raised** on every invalid input from the user. i.e. If an user enters an invalid or wrong input then it prompts the user the respective message and asks the user to try again.

## Summary_Table

SL no |    Tasks    | Issuess Raised |Issues Resolved|No Test Cases|Test Case Pass
-----|-----------------------|---------|----------|------|------
| 01 | Encapsulation (used 3 classes) | X        | X      | 6  | 6
| 02 | Inharitance used(multilevel and multiple) check line no 61 and 226 of [mini_project_main.py](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/mini_project_main.py) | X        | X      | 6  | 6
| 03 | Exception Handling done.(ValueError and user defined) check line number 199 and 271 of [mini_project_main.py](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/mini_project_main.py) | X        | X      | 6  | 6
| 04 | Pylint done, [pylint_Score_report](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/pylint_n_pytest_report/pylint_report.txt): 9.11/10 | X        | X      | 6  | 6
| 05 | Tesing done of 6 functions with various test cases, [Pytest_output_reppport](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/pylint_n_pytest_report/pytest_report.txt) | X        | X      | 6  | 6

## folder_structure

Folder        | description
--------------| ----------------------------------------------
[Implementation](https://github.com/99004351-Debashish/Advanced_Python_mini_project/tree/master/Implementation)        | This folder contains the source code with test file and excel files.
[ScreenShots](https://github.com/99004351-Debashish/Advanced_Python_mini_project/tree/master/Screen_shots)        | screenshots of the code output are placed here.
[pylint_n_pytest_report](https://github.com/99004351-Debashish/Advanced_Python_mini_project/tree/master/pylint_n_pytest_report)        | pylint score report and pytest output reorts are placed here.

* pylint score and pytest output are also printed in [Readme file of Implementation folder](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/readme.md).

## Directory_Tree

```

├── Implementation
│   ├── Advanced_python_mini_project.xlsx
|   ├── Outputs.xlsx
│   ├── mini_project_main.py
│   ├── my_test.py
|   ├── readme.md
|   └── requirements.txt
|   
├── ScreenShots
|   ├── 10_pytest_with_verbose.png
|   ├── 11_pytest_with_verbose_n_s.png
|   ├── 12_pytest_with_verbose_n_s.png
|   ├── 1_select_ps_number.png
|   ├── 2_invalid_ps_entered.png
|   ├── 3_select_sheet.png
|   ├── 4_char_valueexception.png
|   ├── 5_invalid_sheet_choice_exception_handling.png
|   ├── 6_data_fetched_n_saved_to_excel.png
|   ├── 7_Excel_output.png
|   ├── 8_select_another_ps_number.png
|   └── 9_exit.png
|
├── pylint_n_pytest_report
|   ├── pylint_report.txt
|   ├── pytest_report.txt
|   └── pytest_verbose_report.txt
|
├── .gitignore
└── README.md

```



