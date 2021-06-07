"""[This file tests the functions used in the project]
"""
from openpyxl import load_workbook
from mini_project_main import MyExcel, MyExcelOperations, SystemOperations

wb = load_workbook('Advanced_python_mini_project.xlsx')    # loading the workbook
ws = wb.active           # gives the active work sheets of the workbook

#====================defining different conditions to test the functions====================

demo_ps= [
['PS_No.'], [99004351], [99004352], [99004353], [99004354], [99004355], [99004356],
[99004357], [99004358], [99004359], [99004360], [99004361], [99004362], [99004363],
[99004364], [99004365]
]
demo_ps_tup = [
('PS_No.',), (99004351,), (99004352,), (99004353,), (99004354,), (99004355,),
(99004356,), (99004357,), (99004358,), (99004359,), (99004360,), (99004361,),
(99004362,), (99004363,), (99004364,), (99004365,)
]
tup_tup = (
('PS_No.',), (99004351,), (99004352,), (99004353,), (99004354,), (99004355,),
(99004356,), (99004357,), (99004358,), (99004359,), (99004360,), (99004361,),
(99004362,), (99004363,), (99004364,), (99004365,)
)
flat_ps = [
99004351,99004352,99004353,99004354,99004355,99004356,99004357,99004358,99004359,
99004360,99004361,99004362,99004363,99004364,99004365]

#===================================Testing of Functions==========================

def test_get_ps_number():
    """[Tests the get_ps_number() function]
    """
    my_excel = MyExcel(wb)
    test_var = my_excel.get_ps_number()
    assert test_var == demo_ps                          # test case 1

def test_display_ps_number():
    """[Tests the display_ps_numbe() function]
    """
    mp_obj = MyExcel(wb)
    assert mp_obj.display_ps_number(demo_ps) is None        # test case 1 for list in list
    assert mp_obj.display_ps_number(demo_ps_tup) is None    # test case 2 for tuple in list
    assert mp_obj.display_ps_number(tup_tup) is None        # test case 3 for tuple in tuple

def test_flatten_ps_number():
    """[tests the flatten ps number function]
    """
    mp_flat = MyExcel(wb)
    test_ps1 = mp_flat.flatten_ps_number([[99004351,99004352],[99004353,99004354]])
    # for 2 values in the inner list
    assert test_ps1 == [99004351, 99004352, 99004353, 99004354]   # test case 1

    test_ps2 = mp_flat.flatten_ps_number([[99004351],[99004352],[99004353]])
    assert test_ps2 == [99004351, 99004352, 99004353] # test case 2 for 1 value in the inner list

def test_display_sheet_names():
    """[tests the display_sheet_names() function]
    """
    mp_sheet = MyExcel(wb)
    assert mp_sheet.display_sheets_names() is None            # test case


def test_get_data():
    """[tests the get_data() function]
    """
    get_data_obj = MyExcelOperations(wb, wb['Sem'], ['Sem'])
    index = get_data_obj.get_rows(ws, 99004351)
    assert get_data_obj.get_data(index) is None                                 # Test case 1

def test_validate_ip():
    """[tests the validate_ip() function]
    """
    sys_op_obj = SystemOperations()
    assert sys_op_obj.validate_ip(99004351, flat_ps) is True    #test case 1
    assert sys_op_obj.validate_ip(99004352, flat_ps) is True    #test case 2
    assert sys_op_obj.validate_ip(99004353, flat_ps) is True    #test case 3
    assert sys_op_obj.validate_ip(99004365, flat_ps) is True    #test case 4
    assert sys_op_obj.validate_ip(0, flat_ps) is False          #test case 5
    # not in the ps list
    assert sys_op_obj.validate_ip(99004350, flat_ps) is False   #test case 6
    assert sys_op_obj.validate_ip(99004366, flat_ps) is False   #test case 7
