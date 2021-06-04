import mini_project_main as mp
from openpyxl import load_workbook

wb = load_workbook('Advanced_python_mini_project.xlsx')    # loading the workbook 
ws = wb.active           # gives the active work sheets of the workbook

"""====================defining different conditions to test the functions===================="""

demo_ps= [['PS_No.'], [99004351], [99004352], [99004353], [99004354], [99004355], [99004356], [99004357], [99004358], [99004359], [99004360], [99004361], [99004362], [99004363], [99004364], [99004365]]
demo_ps_tup = [('PS_No.',), (99004351,), (99004352,), (99004353,), (99004354,), (99004355,), (99004356,), (99004357,), (99004358,), (99004359,), (99004360,), (99004361,), (99004362,), (99004363,), (99004364,), (99004365,)]
tup_tup = (('PS_No.',), (99004351,), (99004352,), (99004353,), (99004354,), (99004355,), (99004356,), (99004357,), (99004358,), (99004359,), (99004360,), (99004361,), (99004362,), (99004363,), (99004364,), (99004365,))

"""===================================Testing of Functions=========================="""

def test_get_ps_number():               
    test_var = mp.get_ps_number(ws)
    assert test_var == demo_ps                          # test case 1

def test_display_ps_number():    
    assert mp.display_ps_number(demo_ps) is None        # test case 1 for list in list
    assert mp.display_ps_number(demo_ps_tup) is None    # test case 2 for tuple in list
    assert mp.display_ps_number(tup_tup) is None        # test case 3 for tuple in tuple

def test_flatten_ps_number():
    test_ps1 = mp.flatten_ps_number([[99004351,99004352],[99004353,99004354]])
    assert test_ps1 == [99004351, 99004352, 99004353, 99004354]   # test case 1 for 2 values in the inner list                   
    
    test_ps2 = mp.flatten_ps_number([[99004351],[99004352],[99004353]])       
    assert test_ps2 == [99004351, 99004352, 99004353] # test case 2 for 1 value in the inner list

def test_display_sheet_names():
    assert mp.display_sheets_names() is None            # test case 


"""================References===================="""
# https://openpyxl.readthedocs.io/en/stable/tutorial.html
# https://www.javatpoint.com/python-openpyxl
# https://code.tutsplus.com/tutorials/how-to-work-with-excel-documents-using-python--cms-25698