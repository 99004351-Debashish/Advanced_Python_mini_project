# Genesis Advanced python project
* Author: Debashish Dash
* Ps number: 99004351
* **Implementation of OOPs concepts and Exception Handling [in this project is Explained Here](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/readme.md#Main-Objective-of-the-project)**

**Workflows**
Build | Code Quality | Unit Testing |
|--------------------|----------------------------|--------------|
|[![Python application](https://github.com/99004351-Debashish/Advanced_Python_mini_project/actions/workflows/python-app.yml/badge.svg)](https://github.com/99004351-Debashish/Advanced_Python_mini_project/actions/workflows/python-app.yml)  | [![flake8](https://github.com/99004351-Debashish/Advanced_Python_mini_project/actions/workflows/flake8.yml/badge.svg)](https://github.com/99004351-Debashish/Advanced_Python_mini_project/actions/workflows/flake8.yml) [![coverage](https://github.com/99004351-Debashish/Advanced_Python_mini_project/actions/workflows/coverage.yml/badge.svg)](https://github.com/99004351-Debashish/Advanced_Python_mini_project/actions/workflows/coverage.yml)  | [![Pytest](https://github.com/99004351-Debashish/Advanced_Python_mini_project/actions/workflows/pytest.yml/badge.svg)](https://github.com/99004351-Debashish/Advanced_Python_mini_project/actions/workflows/pytest.yml) |

----
## Contents
* [1_About](#1_About)
* [2_Summary Table](#2_Summary_Table)
* [3_Folde Structure](#3_folder_structure)
* [4_Directory Tree](#4_Directory_Tree)
* [5_Installations_and_Run_the_code](#5_Installations_and_Run_the_code)
* [6_Screen Shots of outputs](#6_Screen_Shots_of_outputs)
* [7_References](#7_References)
----
## 1_About
* This project is an appliction that fetch data from an excel sheet and stores the fetched data in another sheet
* It first asks the user to enter the Ps number of which he/she wants to fetch the data.
* Then it asks the user to enter the sheet name from which sheet he/she wants to fetch data.
* Then it fetch the data from the respective sheet and prints in the screen and also writes those data to another excel sheet called Outputs.xlsx
* user also gets an **option to enter another sheet name** to fetch data or he/she can **move back if he/she wants to fetch data from a different ps number** or he/she **can exit** the code.
* **Exceptions** are **Raised** on every invalid input from the user. i.e. If an user enters an invalid or wrong input then it prompts the user the respective message and asks the user to try again.

## 2_Summary_Table

SL no |    Tasks    | Issuess Raised |Issues Resolved|No Test Cases|Test Case Pass
-----|-----------------------|---------|----------|------|------
| 01 | **Encapsulation** (used 3 classes) | X        | X      | 6  | 6
| 02 | **Inharitance** used(**multilevel** and **multiple**) check line no 61 and 226 of [mini_project_main.py](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/mini_project_main.py) | X        | X      | 6  | 6
| 03 | **Exception Handling** done.(**ValueError** and **user defined**) check line number 199 and 271 of [mini_project_main.py](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/mini_project_main.py) | X        | X      | 6  | 6
| 04 | Pylint done, [pylint_Score](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/pylint_n_pytest_report/pylint_report.txt): 9.11/10 | X        | X      | 6  | 6
| 05 | Tesing done of 6 functions with various test cases, [Pytest_output_reppport](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/pylint_n_pytest_report/pytest_report.txt) | X        | X      | 6  | 6
| 06 | [Code coverage report](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/pylint_n_pytest_report/code_coverage.txt), coverage: 45%(functions which takes user inputs cant be tested using pytest so those are tested manually) | X        | X      | 6  | 6
| 07 | Docstring added in all function and class | X        | X      | 6  | 6
| 08 | Github workflows added | X        | X      | 6  | 6

## 3_folder_structure

Folder        | description
--------------| ----------------------------------------------
[Implementation](https://github.com/99004351-Debashish/Advanced_Python_mini_project/tree/master/Implementation)        | This folder contains the source code with test file and excel files.
[ScreenShots](https://github.com/99004351-Debashish/Advanced_Python_mini_project/tree/master/Screen_shots)        | screenshots of the code output are placed here.
[pylint_n_pytest_report](https://github.com/99004351-Debashish/Advanced_Python_mini_project/tree/master/pylint_n_pytest_report)        | pylint score report and pytest output reorts are placed here.

* [pylint score](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/readme.md#pylint_score) and [pytest output](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/readme.md#pytest_output). are also printed in Readme file of Implementation folder

## 4_Directory_Tree

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

-----
## 5_Installations_and_Run_the_code

The code is written in Python 3.8.8 and the Os used is Ubuntu 20.04. If you dont have python installed you can find it [here](https://www.python.org/downloads/).
If you are using a lower version of python then you can upgrade using the pip package, ensuring you have latest version of pip.
* To run this project you need to first [clone](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository

```
# clone the repo
$ git clone https://github.com/99004351-Debashish/Advanced_Python_mini_project.git

# Activate your virtual env (given command is for linux, you can google for windows)
$ source virtualenvironment/project_1/bin/activate

*************************************************
# change the working directory to Implementation
$ cd Implementation
*************************************************

=================================
# install the requirements( ensuring you have activated your virtual env)
$ pip3 install -r requirements.txt
=================================

**(make sure u are inside implementation directory)**

# run the code in linux system
$ python3 mini_project_main.py 

# run the code in windows system
$ python mini_project_main.py

# Pytest (same for both os)
$ pytest my_test.py 

# Check pylint score (current_Score: 9.11/10)
$ pylint mini_project_main.py
```
----
## 6_Screen_Shots_of_outputs
* All the Screen shots are also present in the [Screen_shots folder](https://github.com/99004351-Debashish/Advanced_Python_mini_project/tree/master/Screen_shots). 

**1 Select Ps Number output**

* available ps numbers from the work book are fetched, converted to list and printed on the screen and prompted a message for the user to enter any of the available ps number

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/1_select_ps_number.png" height="500" width="950"> 

**2 What if user entered an invalid Ps number..??**

* If the user enters anything other than the available ps numbers then the following output is shown to user and user is asked to try again, This step was done using **Exception handling**.

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/2_invalid_ps_entered.png" height="500" width="950"> 

**3 Select Sheet Option**

* now after entering the correct ps number the user is asked to enter the sheet from which the user wants to fetch data.

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/3_select_sheet.png" height="500" width="950"> 

**4 What If the user enters an alphabet by mistake..??**

* If the user enters an alphabet by mistake, then the user is prompted with **ValueError exception** and asked to try again. This step also includes Exception Handling.

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/4_char_value_exception.png" height="500" width="950">

**5 What if user enters invalid sheet choice**

* If the user enters invalid sheet choice then the user will be prompted a message saying Invalid input please try again and the user is asked to enter his choice again.

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/5_invalid_sheet_choice_exception_handling.png" height="500" width="950">

**6 Data is fetched on entering of correct sheet number**

* If the user enters a correct choice for the sheet then a list containing the data of the respective PS number of the respective sheet is displayed in the screen along with **a message that says this data is also inserted in to the [Output.xlsx](https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Implementation/Outputs.xlsx) file.** as shown in the below screenshot.
* user can check the Outputs.xlsx file whether the data is inserted or not.
* Along with the data, the Ps number and the sheet name is also saved for a better understanding of the Excel data.(**This is an Extra step performed by me that wasn't asked in the Requirement statement**)

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/6_data_fetched_n_saved_to_excel.png" height="500" width="950">

**7 Check the Excel output**

* As mentioned in the previous point, the data is saved in the `Outputs.xlsx` file now user can open the file and check whether his/her data is stored or not.
* **NOTE 1: IN the given below screenshot of Outputs.xlsx file till row 24 the datas were inserted during the previous runs of the code when the code was being tested.**
* **Note 2: As this can be varified from the previos screen shot of point 6 that the data stored in the output file with ps number `99004361` and the sheet is `PL`. and ad the previous 24 rows are of the previous run the data can be found in the 25th row.**

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/7_Excel_output.png" height="500" width="950">

**8 After saving a data what next..??**

* After saving a data in the `Outputs.xlsx` file the user can also enter another data from different sheet
* Or the user can go back to the Ps number menu to enter another ps number and fetch its data.
* Or the user can exit the code by pressing 0.

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/8_select_another_ps_number.png" height="500" width="950">

**8 Exit the code**

* If user wants to exit the application, he/she can simply do this by pressing 0, as suggested in the screen.

<img src="https://github.com/99004351-Debashish/Advanced_Python_mini_project/blob/master/Screen_shots/9_exit.png" height="500" width="950">

## 7_References
* [openpyxl Documentation](https://openpyxl.readthedocs.io/en/stable/tutorial.html)
* [java T Point](https://www.javatpoint.com/python-openpyxl)
* [tutsplus](https://code.tutsplus.com/tutorials/how-to-work-with-excel-documents-using-python--cms-25698)

