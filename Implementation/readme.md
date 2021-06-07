## contents

* [OOPs Concepts used in this project](#OOPs-Concepts-used-in-this-project)
* [Exception Handling used in this project](#Exception-Handling-used-in-this-project)
* [pylint_score](#pylint_score)
* [pytest_output](#pytest_output)

----
## Main Objective of the project
### OOPs Concepts used in this project
* Encapsulation is used by using 4 classes.
    * class SysytemOperations
    * class MyExcel
    * class MyExcelOperations
    * class Runner
* Multi-level Inheritance and Multiple Inheritance Implemented.
    * class MyExcel inherits SystemOperations class
    * class Runner inherits both MyExcel and MyExcelOperations i.e multiple inheritance
* Static methods are also defined inside SystemOperations class

### Exception Handling used in this project
* In run() method of the Runner class
    * When user enters choice for sheet number then ValueError exception is handled.
    * When user enters a char value then ValueError Exception is raised and user is prompted to enter a valid value
    * When user enters any other value other than the suggested ones then a user defined Exception is raised with a message to try again...
* In ExcelOperations() method of the MyExcelOperations class
    * Here the user input is checked
    * If it is not available in the Ps number options then user defined exception is raised.
    * The exception prints a message saying enter a valid Ps number and try again.
[Go back to main readme]
----
## pylint_score

* **pylint mini_project_main.py**

**=================================================================================**
```
************* Module mini_project_main
mini_project_main.py:44:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:67:22: W0621: Redefining name 'work_book' from outer scope (line 335) (redefined-outer-name)
mini_project_main.py:87:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:105:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:131:22: W0621: Redefining name 'work_book' from outer scope (line 335) (redefined-outer-name)
mini_project_main.py:139:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
mini_project_main.py:157:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:173:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:229:23: W0621: Redefining name 'work_book' from outer scope (line 335) (redefined-outer-name)
mini_project_main.py:229:4: W0231: __init__ method from base class 'MyExcel' is not called (super-init-not-called)
mini_project_main.py:229:4: W0231: __init__ method from base class 'MyExcelOperations' is not called (super-init-not-called)
mini_project_main.py:234:4: R0914: Too many local variables (17/15) (too-many-locals)
mini_project_main.py:234:4: R0912: Too many branches (15/12) (too-many-branches)
mini_project_main.py:234:4: R0915: Too many statements (81/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.21/10 (previous run: 9.21/10, +0.00)
=================================================================================
```
**=================================================================================**

* **pylint Implementation/**
**==================================================================================**
```
************* Module Implementation.mini_project_main
Implementation/mini_project_main.py:44:4: R0201: Method could be a function (no-self-use)
Implementation/mini_project_main.py:67:22: W0621: Redefining name 'work_book' from outer scope (line 352) (redefined-outer-name)
Implementation/mini_project_main.py:87:4: R0201: Method could be a function (no-self-use)
Implementation/mini_project_main.py:105:4: R0201: Method could be a function (no-self-use)
Implementation/mini_project_main.py:131:22: W0621: Redefining name 'work_book' from outer scope (line 352) (redefined-outer-name)
Implementation/mini_project_main.py:139:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
Implementation/mini_project_main.py:157:4: R0201: Method could be a function (no-self-use)
Implementation/mini_project_main.py:173:4: R0201: Method could be a function (no-self-use)
Implementation/mini_project_main.py:200:12: W0105: String statement has no effect (pointless-string-statement)
Implementation/mini_project_main.py:233:23: W0621: Redefining name 'work_book' from outer scope (line 352) (redefined-outer-name)
Implementation/mini_project_main.py:233:4: W0231: __init__ method from base class 'MyExcel' is not called (super-init-not-called)
Implementation/mini_project_main.py:233:4: W0231: __init__ method from base class 'MyExcelOperations' is not called (super-init-not-called)
Implementation/mini_project_main.py:238:4: R0914: Too many local variables (17/15) (too-many-locals)
Implementation/mini_project_main.py:272:28: W0105: String statement has no effect (pointless-string-statement)
Implementation/mini_project_main.py:242:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
Implementation/mini_project_main.py:238:4: R0912: Too many branches (17/12) (too-many-branches)
Implementation/mini_project_main.py:238:4: R0915: Too many statements (93/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.26/10 (previous run: 9.26/10, +0.00)
```
**=================================================================================**
----
## pytest_output

* **pytest -v my_test.py**

**=================================================================================**
```
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3.8
cachedir: .pytest_cache
rootdir: /home/deba/Desktop/LTTS/Advance_python/Advance_Python_project/Implementation
plugins: cov-2.12.0
collecting ... collected 6 items

my_test.py::test_get_ps_number PASSED                                    [ 16%]
my_test.py::test_display_ps_number PASSED                                [ 33%]
my_test.py::test_flatten_ps_number PASSED                                [ 50%]
my_test.py::test_display_sheet_names PASSED                              [ 66%]
my_test.py::test_get_data PASSED                                         [ 83%]
my_test.py::test_validate_ip PASSED                                      [100%]

============================== 6 passed in 0.31s ===============================
```
**=================================================================================**

