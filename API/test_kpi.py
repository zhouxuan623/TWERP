# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_kpi.py
2020/3/11 14:07
@Desc:
"""
import  xlrd
workbook= xlrd.open_workbook("d:\\爱商远程办公情况汇总.xlsx")
sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
work_sheet=workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
for i in range(work_sheet.nrows):
    for j in range(work_sheet.ncols):
        print (work_sheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()


