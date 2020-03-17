# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_param.py
2020/3/9 16:36
@Desc:
"""

import pytest

@pytest.mark.parametrize(('x','y'),[(1,2),(3,4)])
def test_sum(x,y):
    print(x+y)

def test_c():
    print ('---执行c-------')

@pytest.mark.zhou
def test_b():
    print ('执行函数test_b')
if __name__ == '__main__':
    pytest.main(['-v','test_param.py',"-m=zhou"])