## contents

* [pylint_score](#pylint_score)
* [pytest_output](#pytest_output)
* [code_coverage](#code_coverage)

----
## pylint_score

* **pylint mini_project_main.py**

**=================================================================================**
```
************* Module mini_project_main
mini_project_main.py:44:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:67:22: W0621: Redefining name 'work_book' from outer scope (line 352) (redefined-outer-name)
mini_project_main.py:87:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:105:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:131:22: W0621: Redefining name 'work_book' from outer scope (line 352) (redefined-outer-name)
mini_project_main.py:139:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
mini_project_main.py:157:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:173:4: R0201: Method could be a function (no-self-use)
mini_project_main.py:200:12: W0105: String statement has no effect (pointless-string-statement)
mini_project_main.py:233:23: W0621: Redefining name 'work_book' from outer scope (line 352) (redefined-outer-name)
mini_project_main.py:238:4: R0914: Too many local variables (17/15) (too-many-locals)
mini_project_main.py:272:28: W0105: String statement has no effect (pointless-string-statement)
mini_project_main.py:242:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
mini_project_main.py:238:4: R0912: Too many branches (17/12) (too-many-branches)
mini_project_main.py:238:4: R0915: Too many statements (93/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.11/10 (previous run: 9.11/10, +0.00)
=================================================================================
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

## code_coverage

* **pytest --cov=. --cov-report term test.py**

**=================================================================================**
```
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/deba/Desktop/LTTS/Advance_python/Advance_Python_project/Implementation
plugins: cov-2.12.0
collected 6 items

my_test.py ......                                                        [100%]

----------- coverage: platform linux, python 3.8.5-final-0 -----------
Name                   Stmts   Miss  Cover
------------------------------------------
mini_project_main.py     192    127    34%
my_test.py                41      0   100%
------------------------------------------
TOTAL                    233    127    45%


============================== 6 passed in 0.38s ===============================
```
* `Note: code coverage is 45% because some functions in the mini_project_main.py takes user input and those functions can not be tested using pytest, Those functions are manually tested.`
**=================================================================================**