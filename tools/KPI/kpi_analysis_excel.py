# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->kpi_analysis_excel.py
2020/3/13 14:24
@Desc:KPI考核数据汇总 解析杜姐发的考核指标信息，转化为分值写入数据库
"""
import xlrd
import pymysql
import sys
import os

filename = os.path.join(os.path.dirname(os.path.dirname(__file__)),'kqfiles',"kpi.xlsx")
workbook = xlrd.open_workbook(filename)
"先格式化excel"
worksheet= workbook.sheets()[1]

nrows = worksheet.nrows
ncols = worksheet.ncols
infos = []
for i in range(1, worksheet.nrows):
    info = {}

    "需求评审通过率"
    demand_nums = worksheet.cell(i, 1).value  # 需求评审>=2满分=1一半分数 其他0分
    if demand_nums > 1:
        demand_judge = 1
    elif demand_nums == 1:
        demand_judge = 0.5
    else:
        demand_judge = 0
    info['demand_judge'] = demand_judge

    "版本公告+版本培训对应系统中的产品发布及培训"
    VersionOfTheAnnouncement = int(worksheet.cell(i, 2).value)  # 版本公告 >=1满分，其他0分
    VersionOfTrain = int(worksheet.cell(i, 3).value)  # 版本培训 >=1 满分，其他零分
    if VersionOfTheAnnouncement >= 1 and VersionOfTrain >= 1:
        ProductLaunchTraining_param = 1
    elif VersionOfTheAnnouncement < 1 and VersionOfTrain < 1:
        ProductLaunchTraining_param = 0
    else:
        ProductLaunchTraining_param = 0.5
    info['product_train'] = ProductLaunchTraining_param

    AnalysisCompetitiveProducts = int(worksheet.cell(i,4).value)  #竞品分析包含两个指标：1 产品市场的调查与研究：一个月两封分析邮件满分，一封得一半。\
    # 2、产品创新 有一封邮件就默认有创新建议，则满分
    if AnalysisCompetitiveProducts >=2:
        ProductMarketAnalysis = 1 #产品市场的调查与研究
        ProductInnovate = 1 #产品创新
    elif AnalysisCompetitiveProducts ==1:
        ProductMarketAnalysis = 0.5
        ProductInnovate =1
    else:
        ProductMarketAnalysis = ProductInnovate = 0
    info['research_and_analyst'] = ProductMarketAnalysis
    info['product_innovative'] = ProductInnovate

    "内部培训"
    ##内部培训分为业务培训和技能培训 暂时设定大于1满分=1一半其他0
    BusinessTraining =int(worksheet.cell(i,5).value)   #内部业务培训
    if BusinessTraining>=1:
        BusinessTraing_param=1
    # elif BusinessTraining ==1:
    #     BusinessTraing_param = 0.5
    else:
        BusinessTraing_param =0
    TechnicalTraining =int(worksheet.cell(i,6).value)   #内部技术培训
    if TechnicalTraining>=1:
        TechnicalTraining_param=1
    # elif BusinessTraining ==1:
    #     TechnicalTraining_param = 0.5
    else:
        TechnicalTraining_param =0
    info['business_training']=BusinessTraing_param
    info['skill_training'] =TechnicalTraining_param

    "市场宣传文案 对应产品推广与宣传字段"
    MarketCopywrite = int(worksheet.cell(i,7).value)   #市场宣传文案
    if MarketCopywrite>0:
        MarketCopywrite_param = 1
    else:
        MarketCopywrite_param = 0
    info['promotion_publicity']=MarketCopywrite_param

    "产品计划明确性 直接填写系数 0 1 "
    ProductPlan_param = worksheet.cell(i,8).value
    info['product_definition'] = float(ProductPlan_param)

    "产品月销售额 填写百分比系数"
    Sale_param = worksheet.cell(i,9).value
    info['product_sale'] =  float(Sale_param)

    "产品帮助文档  直接填写系数0,1 1满分"
    Doc_help = worksheet.cell(i,10).value
    info['product_doc']=Doc_help

    "产品线工作安排与管理"
    work_management = worksheet.cell(i,11).value
    info['work_management'] = float(work_management)

    "产品使用率"
    usage_rate = worksheet.cell(i,12).value
    info['usage_rate'] = float(usage_rate)

    "已付费流失率"
    lossing_customer = worksheet.cell(i,13).value
    info['lossing_customer'] = float(lossing_customer)



    department = worksheet.cell(i,0).value
    if department=='ERP3.0':
        info['department']='新erp组'
    elif department =='上架营销':
        info['department']='刊登组'
    else:
        info['department']='IBIZ开发组'
    infos.append(info)
    # infos[worksheet.cell(i,0).value]=info
print (infos)

"数据通过SQL插入进去"

connection = pymysql.connect(host='10.0.6.170',
                             port=3306,
                             user='root',
                             password='TOBO@123',
                             db='django1',
                             charset='utf8')
kpi_year=input("请输入考核年份")
kpi_month=input('请输入考核月份')
# 获取游标
cursor = connection.cursor()
SQL="""
SELECT demand_judge '需求评审通过率', product_train '产品发布及培训',research_and_analyst '产品市场的调查与研究',
product_innovative '产品创新',business_training '内部业务培训',skill_training '内部技术培训'
,promotion_publicity '产品推广与宣传',product_definition '产品计划明确性',product_sale '产品月销售额',product_doc '产品帮助文档'
from django1.devs_kpiinfos where kpi_year='2020' and kpi_month='2';"""
"插入数据，默认bug系数都是1，默认自动化完成率为1"
for info in infos:
    demand_judge = info['demand_judge']
    product_train = info['product_train']
    research_and_analyst = info['research_and_analyst']
    product_innovative = info['product_innovative']
    business_training = info['business_training']
    skill_training = info['skill_training']
    promotion_publicity= info['promotion_publicity']
    product_definition= info['product_definition']
    product_sale= info['product_sale']
    product_doc = info['product_doc']
    work_management = info['work_management']
    usage_rate = info['usage_rate']
    lossing_customer = info['lossing_customer']
    department = info['department']
    SQL_UPDATE=f"""update devs_kpiinfos set
    demand_judge='{demand_judge}' ,
    product_train = '{product_train}' ,
    research_and_analyst = '{research_and_analyst}'
    , product_innovative = '{product_innovative}'
    , business_training = '{business_training}'
    , skill_training = '{skill_training}'
    , promotion_publicity ='{promotion_publicity}'
    , product_definition = '{product_definition}'
    , product_sale = '{product_sale}',product_doc='{product_doc}',
    work_management = '{work_management}',
    usage_rate = '{usage_rate}',
    lossing_customer = '{lossing_customer}', auto_test=1 , bug_param=1
    where kpi_year='{kpi_year}' and kpi_month='{kpi_month}'
    and department='{department}' ;"""
    print(SQL_UPDATE)
    cursor.execute(SQL_UPDATE)
confirm_input = input(f"即将导入{kpi_year}年{kpi_month}的数据，输入'Y'确认，输入'N'取消")
if confirm_input.upper()=='Y':
    connection.commit()
    connection.close()
    sys.stdout.write("导入成功,请刷新查看")
else:
    connection.rollback()
    sys.stdout.write('导入失败')

















