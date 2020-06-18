# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->kqjiexi.py
2020/6/15 10:44
@Desc:
"""
import os
import xlrd
import pymysql
import sys
print(os.path.dirname(__file__))
files=os.path.join(os.path.dirname(__file__),"kqfiles","202005.xlsx")
print(files)
"""
"吴路浠",'李兴恩' 李华 方家威 转外包，不纳入考核
"""
devs={'IBIZ开发组':['白尧','黄春','曾小云'],
        '新erp组':['黄庆坤','王玉清','罗甘',"喻场"],
      #方家威从2020年2月开始计算 之前的都没计入，算作了运维 杜姐批准安排两人人力算运维 方家威+,'喻场'
        '刊登组':['刘玺','张浩','杨达奇']}
"李兴恩  李华 吴路浠不再记作半个人力2019/10/14  '杨达奇',研究爬虫"
half_dev=['张浩',"黄庆坤","杨达奇",'王玉清','罗甘']   #需要维护  加入此list中的人，不能把他从产品线组里删除
workbook = xlrd.open_workbook(files)
# table = workbook.sheet_by_name('Sheet1')
table = workbook.sheets()[0]
nrows= table.nrows
ncols = table.ncols
values={}
names = []
for i in range(1,nrows):
    name = table.cell(i,1).value   #获取人员信息 姓名(2列)
    if name not in names:
        names.append(name)

for name in names:
    working_infos = {}  #存储每个人员的打卡记录
    for i in range(1,nrows):
        name_1 = table.cell(i,1).value  #姓名
        if name == name_1:
            working_date=table.cell(i,0).value  #日期
            tmp= str(working_date).split('/')[-1]
            "全量读取"
            start_time = table.cell(i, 3).value  #上班时间
            endtime = table.cell(i, 4).value  #下班时间
            working_infos[working_date] = (start_time, endtime)
    values[name]=working_infos

"先统计每个人的工作日"
dev_working={} #存储开发人员的一个月的工作日
for key,value in values.items():
    dev_name = key
    count=0
    for w_date,w_value in value.items():
        if w_value[0]!='--' or w_value[1]!='--':  #有早上或者晚上的打卡记录,就算一天的工时
            count+=1
    dev_working[dev_name]=count
print (dev_working)

parent_working={}  #统计产品线的工作人天
for parent_name,devs in devs.items():
    """
    parent_name:产品线
    devs  开发人员分组信息
    dev_working ｛开发人员:总工作日｝
    """
    # if parent_name=='分销平台组':
    #     fenxiao=0
    #     for dev_key,dev_value in dev_working.items():
    #         # print dev_key
    #         if str(dev_key.encode('utf-8')) in devs:
    #             print (dev_key, dev_value)
    #             if str(dev_key.encode('utf-8')) in half_dev:  #半个人力
    #                 dev_value=dev_value/2.0
    #             fenxiao+=dev_value
    #     parent_working["分销平台组"]=fenxiao
    if parent_name=='IBIZ开发组':
        erp=0
        for dev_key,dev_value in dev_working.items():
            # print dev_key
            if dev_key in devs:
                if dev_key in half_dev:  #半个人力
                    dev_value=dev_value/2.0
                erp+=dev_value
        parent_working["IBIZ开发组"]=erp

    if parent_name=='新erp组':
        newerp=0
        for dev_key,dev_value in dev_working.items():
            # print dev_key
            if dev_key in devs:
                if dev_key in half_dev:  #半个人力
                    dev_value=dev_value/2
                newerp+=dev_value
        parent_working["新erp组"] = newerp
    if parent_name=='刊登组':
        listing_days=0
        for dev_key,dev_value in dev_working.items():
            # print dev_key
            if dev_key in devs:
                if dev_key in half_dev:  #半个人力
                    dev_value=dev_value/2.0
                listing_days+=dev_value
        parent_working["刊登组"] = listing_days
    #
    # if parent_name=='物流组':
    #     shipping=0
    #     for dev_key,dev_value in dev_working.items():
    #         if str(dev_key.encode('utf-8')) in devs:
    #             if str(dev_key.encode('utf-8')) in half_dev:  #半个人力
    #                 dev_value=dev_value/2.0
    #             shipping+=dev_value
    #     parent_working["物流组"] = shipping

for parent,value in parent_working.items():
    print (parent,value)

"把工时插到数据库"
kpi_year=input("请输入年份")
kpi_month=input("请输入月份")

_connect = pymysql.connect(host="10.0.6.170", user="root", password="TOBO@123",
                           database="django_test", port=3306)
for parent,workingtime in parent_working.items():
    update_workingtime=f"""update django_test.devs_kpiinfos set working_checking={workingtime},bug_param=1,auto_test=1
     WHERE kpi_year={kpi_year} and kpi_month={kpi_month} and department='{parent}' """
    _connect.cursor().execute(update_workingtime)
confirm_input = input(f"即将导入{kpi_year}年{kpi_month}的数据，输入'Y'确认，输入'N'取消")
if confirm_input.upper()=='Y':
    _connect.commit()
    _connect.close()
    sys.stdout.write("导入成功,请刷新查看")
else:
    _connect.rollback()
    sys.stdout.write('导入失败')

