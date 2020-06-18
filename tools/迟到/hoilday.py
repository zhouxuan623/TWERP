# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->hoilday.py
2020/6/16 14:35
@Desc:
"""
import os
def hoildays_list():
    """
    :return:节假日+周末
    """
    hoilday=os.path.join(os.path.dirname(os.path.dirname(__file__)),'kqfiles','hoilday')
    with open(hoilday,'r') as file:
        results=file.readlines()
    hoildays=[]
    for i in results:

        hoildays.append(i[:4]+'/'+i[4:6]+'/'+i[6:8])
    return hoildays
print (hoildays_list())