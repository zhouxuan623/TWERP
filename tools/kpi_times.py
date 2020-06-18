#coding:utf-8
"""
@Author : zhouxuan
@Time : 2019/1/10 11:34
@File : leader.py
@note : 给项目负责人发送的信息
"""
import pandas as pd
import codecs
from lxml import  etree
from datetime import  datetime


import  xlrd
import  os
# files=os.path.join(os.path.dirname(os.path.dirname(__file__)),'files/kaoqin.xls').replace('\\','/')
# print files
workbook = xlrd.open_workbook('202001_1.xls')
# table = workbook.sheet_by_name('Sheet1')
table = workbook.sheets()[0]
nrows= table.nrows
ncols = table.ncols
values={}
names = []
"""
4yue   ibiz=22+20+22+24+21=109
xin erp 16/2+21+20+22=71
刊登：20+22/2+22/2+22

"""
devs={'IBIZ开发组':['白尧','黄春','曾小云',"吴路浠",'李兴恩'],
        '新erp组':['黄庆坤','王玉清','罗甘','方家威'],
      #方家威从2020年2月开始计算 之前的都没计入，算作了运维 杜姐批准安排两人人力算运维 方家威+,'喻场'
        '刊登组':['刘玺','张浩','杨达奇','李华']}
"李兴恩  李华 吴路浠不再记作半个人力2019/10/14  '杨达奇',研究爬虫"
half_dev=['张浩',"黄庆坤","杨达奇","方家威"]   #需要维护  加入此list中的人，不能把他从产品线组里删除


for i in range(1,nrows):
    name = table.cell(i,2).value   #获取人员信息 姓名
    if name not in names:
        names.append(name)
for name in names:
    working_infos = {}  #存储每个人员的打卡记录
    for i in range(1,nrows):
        # for j in range(ncols):
            # if table.cell(0,j).value==u'姓名':
            #     print table.cell(i,j).value
        name_1 = table.cell(i,2).value  #姓名
        if name == name_1:
            working_date=table.cell(i,3).value  #日期
            tmp= working_date.split('/')[-1]

            "指定日期时候输出"
            # if int(working_date.split('/')[-1])>24:  #统计日期从25日开始
            #     start_time = table.cell(i,6).value
            #     endtime = table.cell(i,7).value
            #     working_infos[working_date]=(start_time,endtime)

            "全量读取"
            start_time = table.cell(i, 6).value  #上班时间
            endtime = table.cell(i, 7).value  #下班时间
            working_infos[working_date] = (start_time, endtime)
            # working_info['working_date'] = table.cell(i,3).value
            # working_info['w_starttime'] = table.cell(i,6).value
            # working_info['w_endtime'] = table.cell(i,7).value
    values[name]=working_infos

"先统计每个人的工作日"
dev_working={} #存储开发人员的一个月的工作日
for key,value in values.items():
    dev_name = key
    count=0
    for w_date,w_value in value.items():
        if w_value[0]!='' or w_value[1]!='':  #有早上或者晚上的打卡记录,就算一天的工时
            count+=1
    dev_working[dev_name]=count
print (dev_working)

# "统计每个人每天的总工时 包含中午的1.5小时"
# dev_working_hours={}
# for key,value in values.items():
#     dev_name = key
#     print dev_name
#     for w_date,w_value in value.items():
#         if w_value[0] !='' and w_value[1]!= '':
#             pass
#             # print w_date,datetime.strptime(w_value[1],'%H:%M')-datetime.strptime(w_value[0],'%H:%M')
#         if w_value[0] !='' and w_value[1]== '':
#             print  w_date
#
#     print '==================================================='


parent_working={}  #统计产品线的工作人天
for parent_name,devs in devs.items():
    """
    parent_name:产品线
    devs  开发人员分组信息
    dev_working ｛开发人员:总工作日｝
    """
    if parent_name=='分销平台组':
        fenxiao=0
        for dev_key,dev_value in dev_working.items():
            # print dev_key
            if str(dev_key.encode('utf-8')) in devs:
                print (dev_key, dev_value)
                if str(dev_key.encode('utf-8')) in half_dev:  #半个人力
                    dev_value=dev_value/2.0
                fenxiao+=dev_value
        parent_working["分销平台组"]=fenxiao
    if parent_name=='IBIZ开发组':
        erp=0
        for dev_key,dev_value in dev_working.items():
            # print dev_key
            if str(dev_key.encode('utf-8')) in devs:
                if str(dev_key.encode('utf-8')) in half_dev:  #半个人力
                    dev_value=dev_value/2.0
                erp+=dev_value
        parent_working["IBIZ开发组"]=erp

    if parent_name=='新erp组':
        newerp=0
        for dev_key,dev_value in dev_working.items():
            # print dev_key
            if str(dev_key.encode('utf-8')) in devs:
                if str(dev_key.encode('utf-8')) in half_dev:  #半个人力
                    dev_value=dev_value/2
                newerp+=dev_value
        parent_working["新erp组"] = newerp
    if parent_name=='刊登组':
        listing_days=0
        for dev_key,dev_value in dev_working.items():
            # print dev_key
            if str(dev_key.encode('utf-8')) in devs:
                if str(dev_key.encode('utf-8')) in half_dev:  #半个人力
                    dev_value=dev_value/2.0
                listing_days+=dev_value
        parent_working["刊登组"] = listing_days

    if parent_name=='物流组':
        shipping=0
        for dev_key,dev_value in dev_working.items():
            if str(dev_key.encode('utf-8')) in devs:
                if str(dev_key.encode('utf-8')) in half_dev:  #半个人力
                    dev_value=dev_value/2.0
                shipping+=dev_value
        parent_working["物流组"] = shipping

for parent,value in parent_working.items():
    print (parent,value)




