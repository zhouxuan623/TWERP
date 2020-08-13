# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->kpi_times.py
2020/7/7 9:53
@Desc:直接读取考勤原文件，解析出需要读取的行信息 写入各产品线的工时，谨慎使用
"""
import xlrd
import os
import pymysql
import sys
excle_name=input("输入要解析的文件名")
filename = os.path.join(os.path.dirname(os.path.dirname(__file__)),'kqfiles',excle_name)
workbook = xlrd.open_workbook(filename)
sheet0 = workbook.sheet_by_name("爱商")
"循环读取数据 不考虑工作日和休息日，只需要有打卡，就记录为正常工时"
"需要考勤的姓名信息汇总"
devs={'IBIZ开发组':['白尧','黄春','曾小云'],
        '新erp组':['黄庆坤','王玉清','罗甘','喻场'],
        '刊登组':['刘玺','张浩','杨达奇']}
half_dev=['张浩',"黄庆坤","杨达奇",'王玉清','罗甘','喻场']   #需要维护  加入此list中的人，不能把他从产品线组里删除
names=[]
for department,name in devs.items():
    names+=name
names_dict={f"{name}":0 for name in names}   #dict格式，汇总最后的结果  开发人员：工时
"提取考核人员的考勤"
"提取列标题"
working_index=[];
for col in range(sheet0.ncols):
    col_name = sheet0.cell(0,col).value
    if col_name == "时间":
        time_index = col
    elif col_name == "姓名":
        name_index = col
    elif col_name == "打卡时间":
        working_index.append(col)
starting_index,ending_index=working_index  #解决excle中两个列名字相同

for i in range(sheet0.nrows):
    k_name = sheet0.cell(i, name_index).value
    k_date = sheet0.cell(i,time_index).value
    k_startingtime = sheet0.cell(i,starting_index).value
    k_endingtime = sheet0.cell(i,ending_index).value
    if k_name in names:
        if ":" in k_startingtime or ":" in k_endingtime:
            names_dict[k_name]+=1

# for key,value in names_dict.items():
#     print (key,":",value)


devs={'IBIZ开发组':['白尧','黄春','曾小云','田野'],
        '新erp组':['黄庆坤','王玉清','罗甘','喻场'],
        '刊登组':['刘玺','张浩','杨达奇']}
half_dev=['张浩',"黄庆坤","杨达奇",'王玉清','罗甘','喻场']   #需要维护  加入此list中的人，不能把他从产品线组里删除
erp2_working_days=0
erp3_working_days=0
listing_working_days=0
for name,working_day in names_dict.items():
    if name in half_dev:
        working_day=working_day/2.00
    if name in devs['IBIZ开发组']:
        erp2_working_days+=working_day
    elif name in devs['新erp组']:
        erp3_working_days+=working_day
    elif name in devs['刊登组']:
        listing_working_days+=working_day

"数据写入"
mysql_connect = pymysql.connect(host="10.0.6.170", user='root', password="TOBO@123",
                 database='django1', port=3306)
con = mysql_connect.cursor()
departments_dic={"IBIZ开发组":erp2_working_days,"新erp组":erp3_working_days,'刊登组':listing_working_days}
kpi_year=input("输入考核年份：")
kpi_month=input("输入考核月份：")
try:
    for department,working_time in departments_dic.items():
        SQL = f"update  django1.devs_kpiinfos set working_checking='{working_time}' where department='{department}' \
        and kpi_year={kpi_year} and kpi_month={kpi_month} "
        con.execute(SQL)
    con.close()
    mysql_connect.commit()
    sys.stdout.write("写入成功")
except Exception as e:
    print (e)
    mysql_connect.rollback()
    sys.stderr.write("写入失败，请检查")
mysql_connect.close()
print (erp3_working_days,erp2_working_days,listing_working_days)
