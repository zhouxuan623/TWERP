
# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test.py
2020/6/16 15:32
@Desc:
"""

import re
# result=re.findall("迟到(.*)分钟","迟到1小时5分钟")
# if '小时' in result[0]:
#     delay=int(result[0].split("小时")[0])*60+int(result[0].split("小时")[1])
# print (delay)
result=[("迟到1小时5分钟",'')]
int(result[0].split("小时")[0]) * 60
int((result[0].split("小时")[1]).replace('分钟',''))