# This file contains main source code
"""
    * [File: mini_project_main.py]
    * [Author: Debashish Dash]
    * [Date: 03-06-2021]
    * 
    * [@copyright (c) 2021]
    *
"""

# importing dependencies 
from openpyxl import workbook, load_workbook

wb = load_workbook('Advanced_python_mini_project.xlsx')    # loading the workbook

ws = wb.active           # gives the active work sheets of the workbook

work_sheets = wb.sheetnames       #storing the worksheet names of the workbook
print(work_sheets)