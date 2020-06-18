# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->chidao.py
2020/6/16 11:20
@Desc:
"""
from hoilday import hoildays_list
import os
import xlrd                           #导入模块
import xlwt
import re
from xlutils.copy import copy

HOILDAYS = hoildays_list()  # 节假日
VIP_NAME = ['夏浩波', '方家威', '施曼', '李兴恩', '李华', "郑迪岸"]  #不需要考核的员工
def analysis_excle(target_file,excelname):
    """
    :param target_file: 需要解析的excel
    :param excelname:  最后生成的excle
    :return:
    """
    wb = xlwt.Workbook(encoding='ascii')
    ws=wb.add_sheet('考勤信息',cell_overwrite_ok=True)
    ws_delay=wb.add_sheet('迟到信息',cell_overwrite_ok=True)
    file=os.path.join(os.path.dirname(os.path.dirname(__file__)),"kqfiles",target_file)
    workbook = xlrd.open_workbook(file)
    table = workbook.sheets()[0]
    nrows= table.nrows
    names = []
    for i in range(1,nrows):
        name = table.cell(i,1).value   #获取人员信息 姓名(2列)
        if name not in names:
            names.append(name)
    daka_list=[]
    delay_infos=[]
    for i in range(1,nrows):
        tmp=[]
        "全量读取"
        checking_time = table.cell(i,0).value #日期
        if checking_time not in HOILDAYS:
            name = table.cell(i,1).value #姓名
            start_time = table.cell(i, 11).value  #上班时间
            endtime = table.cell(i, 14).value  #下班时间
            checking_status=table.cell(i,12).value  #打卡状态 有迟到的抽出来
            "把迟到的数据抽出来"
            if "迟到" in checking_status:
                result = re.findall("迟到(.*)(分钟){0,1}", checking_status)
                print (result[0][0])
                try:
                    if '小时' in result[0][0]:
                        delay_time = int((result[0][0]).split("小时")[0]) * 60 + int(((result[0][0]).split("小时")[1]).replace('分钟',''))
                    else:
                        delay_time=int((result[0][0]).replace('分钟',''))
                    delay_infos.append([name, checking_time, delay_time])
                except:
                    print (result)
            elif '未打卡' in checking_status:
                delay_time = '未打卡'
                delay_infos.append([name, checking_time, delay_time])
            tmp=[checking_time,name,start_time,endtime,checking_status]
            daka_list.append(tmp)
    row_index=0
    for infos in daka_list:
        for j in range(len(infos)):
            ws.write(row_index, j, label=infos[j])
        row_index+=1
    delay_index=0
    ws_delay.write(0,0,label='姓名')
    ws_delay.write(0,1,label='考勤日期')
    ws_delay.write(0,2,label='考勤异常')
    ws_delay.write(0,3,label='备注')
    for infos in delay_infos:
        for j in range(len(infos)):
            ws_delay.write(delay_index+1, j, label=infos[j])
        delay_index+=1
    wb.save(os.path.join(os.path.dirname(os.path.dirname(__file__)),'kqfiles',excelname))


def clc_delay_times(target_file):
    """迟到人员信息"""
    "解析生成的excle,生成list"
    file_excel=os.path.join(os.path.dirname(os.path.dirname(__file__)),'kqfiles',target_file)
    data = xlrd.open_workbook(file_excel)
    table=data.sheets()[1] #迟到sheet
    nrows=table.nrows
    delay_infos=[]
    for i in range(1,nrows):
        notes=table.cell(i,3).value
        if notes=="":
            "正常请假无异常"
            name=table.cell(i,0).value
            kq_date=table.cell(i,1).value
            delay_time=table.cell(i,2).value
            delay_infos.append([name,kq_date,delay_time])
    names=[]
    for info in delay_infos:
        if info[0] in VIP_NAME:
            pass
        elif info[0] not in names:
            names.append(info[0])
    "不用考核名单"
    result=[]

    for name in names:
        delay_count=0
        greater15_count=0
        less15_count=0
        less5_count=0
        unchecking_count=0  #未打卡
        times=0   #迟到累计时间
        less15times=[]  #迟到小于15分钟时间
        less5times=[]  #迟到小于5分钟时间
        for info in delay_infos:
            if name==info[0]:
                delay_time = info[2]  # 迟到时间
                if type(delay_time)==float:
                    if delay_time>15:
                        times+=delay_time  #大于15的直接扣钱，不计入累计迟到次数
                    elif delay_time>5 and delay_time<=15:
                        less15_count+=1
                        delay_count+=1
                        less15times.append(delay_time)
                    else:
                        less5_count+=1
                        delay_count+=1
                        less5times.append(delay_time)
        less15times.sort(reverse=True)
        less5times.sort(reverse=True)
        if delay_count>5:
            target_time=0  #累计迟到时间
            if less15_count>3:
                target_time=sum(less15times[3:])+sum(less5times[2:])
            else:
                target_time=sum(less5times[6-less15_count:])  # 3+3-less15count 15分钟的不够，直接扣小于5的
            times+=target_time
        else:
            times+=sum(less15times[3:])
        if times>0:
            print (name,times)
            result.append([name,times])
        "把数据写到excel中"
    return result


def copy_and_write_excel(filename,dest_file):
    file=os.path.join(os.path.dirname(os.path.dirname(__file__)),'kqfiles')
    rb=xlrd.open_workbook(os.path.join(file,filename))
    wb=copy(rb)
    ws=wb.add_sheet("考勤汇总",cell_overwrite_ok=True)
    result=clc_delay_times(os.path.join(file,filename))
    ws.write(0,0,label='姓名')
    ws.write(0,1,label='扣减后迟到时长')
    for i in range(len(result)):
        ws.write(i+1,0,label=result[i][0])
        ws.write(i+1,1,label=result[i][1])
    wb.save(os.path.join(file,dest_file))

if __name__ == '__main__':
    """
    执行说明 注意两个不能一起执行 先执行analysis_excle('05.xlsx','debu1.xlsx') 其中前面是原始考核excle，后面是解析后的excel
    解析后的excel先给喻蓉，让喻蓉把备注列填写清楚后，再来执行copy_and_write_excel('debu1.xlsx','zhou1.xlsx') 
    这样最后得出的zhou1.xlsx 就是最后给喻蓉的结果
    """
    # analysis_excle('05.xlsx','debu1.xlsx')
    copy_and_write_excel('debu1.xlsx','zhou1.xlsx')












