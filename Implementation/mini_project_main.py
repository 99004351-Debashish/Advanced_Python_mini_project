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
from openpyxl import load_workbook #, workbook

wb = load_workbook('Advanced_python_mini_project.xlsx')    # loading the workbook

ws = wb.active           # gives the active work sheets of the workbook

def get_ps_number(ip_ws):
    """[fetch the data from the first column of the excel]

    Args:
        ip_ws ([type: object]): [active worksheet]

    Returns:
        [type: list]: [data of the 1st column in the excel sheet, return as list]
    """

    ps_nums=[]
    for row in ip_ws.iter_rows(min_row=1, max_col=1, max_row=16, values_only=True):
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
# End of function


def display_ps_number(flat_ps):
    """[prints the ps ids in the terminal]

    Args:
        flat_ps ([type: list]): [1-d converted form of the 2-D list data]
    """
    for ps_num in flat_ps:
        print(ps_num)
# End of Function


def display_sheets_names():
    """[stores and Displays the names of the sheets]
    """
    work_sheets = wb.sheetnames       #storing the worksheet names of the workbook
    opt=1
    for sheet in work_sheets:
        print("\npress ",opt," for ",sheet)
        opt+=1
# End of Function

def get_rows(work_s,ps_num):
    for row in work_s.rows:
        if row[0].value == ps_num:
            return row
# End of function

#var = get_rows(wb['Sem'], 99004351)
def get_data(row_index):
    index_data=[]
    for index in range(1,20):
        index_data.append(row_index[index].value)
    print(index_data)

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

def validate_ip(user_ip,flatten_ps):
    int_user_ip=int(user_ip)
    if int_user_ip in flatten_ps:
        return True
    return False
# End of function

def excel_operation(work_sheet_name):
    user_choice=" "
    while user_choice != '1':
        print("\nEnter the PS number from the below list:\n")
        print(20*'=')
        ps_num = get_ps_number(work_sheet_name)
        flatten_ps = flatten_ps_number(ps_num)
        display_ps_number(flatten_ps)
        print(20*'=')
        print("\nEnter the ps number to get its data")
        print("\nOr press 0 to exit")
        print("\nOr press 1 to go to Sheet selection menu:")
        user_choice = input("\nEnter Your Choice: ")
        screen_clear()
        if user_choice == '0':
            system_exit()
        if user_choice == '1':
            break
        if user_choice in str(ps_num):
            if validate_ip(user_choice,flatten_ps):
                print("="*40)
                print("\n\n")
                print("\nEntered Ps is: ", user_choice, "and respective scores are:" )
                row_index = get_rows(work_sheet_name, int(user_choice))
                get_data(row_index)
                print("\n\n")
                print("="*40)
                print("Enter Another PS ????")
            else:
                print(20*'=')
                print("Oops You have entered an invalid choice !!")
                print("\nPlease Try again...")
                print(20*'=')
        else:
            print(20*'=')
            print("Oops You have entered an invalid choice !!")
            print("\nPlease Try again...")
            print(20*'=')
# End of function


def main():
    """[this is the function that performs all the tasks in a sequence]
    """
    sheet_score = wb['Sem']
    sheet_hobbies = wb['Hobbies']
    sheet_cities = wb['Cities']
    sheet_pl = wb['PL']
    sheet_domain = wb['Domain']
    while True:
        print("\nSelect the Sheet:")
        print(30*'=')
        display_sheets_names()
        print("\nOr press 0 to exit: \n")
        print(30*'=')
        sheet_choice = input("\nPlease Enter your choice:")
        screen_clear()
        if sheet_choice == '1':
            excel_operation(sheet_score)
        elif sheet_choice == '2':
            excel_operation(sheet_hobbies)
        elif sheet_choice == '3':
            excel_operation(sheet_cities)
        elif sheet_choice == '4':
            excel_operation(sheet_pl)
        elif sheet_choice == '5':
            excel_operation(sheet_domain)
        elif sheet_choice == '0':
            system_exit()
        else:
            print(30*'=')
            print("ops..!! You have entered an invalid choice")
            print("Please Try again... :(")
            print(30*'=')
            #main()
            continue

if __name__ == "__main__":
    main()
