# This file contains main source code
"""
    * [File: mini_project_main.py]
    * [Author: Debashish Dash]
    * [Date: 03-06-2021]
    * 
    * [@copyright (c) 2021]
    *
""" 
import os
import sys
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter 

wb = load_workbook('Advanced_python_mini_project.xlsx')    # loading the workbook 

ws = wb.active           # gives the active work sheets of the workbook

class wbSet:
    pass
"""====================== Rough ======================"""
work_sheets = wb.sheetnames       #storing the worksheet names of the workbook
print(work_sheets)

#print(ws['A1'].value)


"""===================================================="""

def get_ps_number(ip_ws):
    ps_nums=[]
    for row in ws.iter_rows(min_row=1, max_col=1, max_row=16, values_only=True):
        ps_nums.append(list(row))
    return ps_nums
# End Of Function

def flatten_ps_number(ps_list):
    """[get_ps_num() fun returns ps nums as 2D list, so this function flatten the list in to 1-D]

    Args:
        ps_list ([type: list]): [It is a 2-D list]

    Returns:
        [type: list]: [Converted 1-D form of the 2-D list is returned]
    """
    flat_ps = []
    # iterating over the list that contains ps nums
    for ps_num in ps_list:
        #appending ps number to the flat list
        flat_ps += ps_num
    return flat_ps
#End of function


def display_ps_number(flat_ps):
    for ps_num in flat_ps:
        print(ps_num)
# End of Function

def screen_clear():
    """
    clears the screen, works in both the os
    """
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
# End of Function


def system_exit():
    """
        [Exits from the code]
    """
    sys.exit("\n\nThank You for visiting... \n\n")
# End of Function

def main():
    print("\nEnter the PS number from the below list:\n")
    print(20*'=')
    ps_num = get_ps_number(ws)
    flatten_ps = flatten_ps_number(ps_num)
    display_ps_number(flatten_ps)
    print(20*'=')
    user_choice = int(input("\nEnter the Ps number: \nOr Enter 0 to exit: "))
    screen_clear()
    if user_choice in ps_num:
        pass
    elif user_choice == 0:
        system_exit()
    else:
        print("Oops You have entered an invalid choice !!")

if __name__ == "__main__":
    main()