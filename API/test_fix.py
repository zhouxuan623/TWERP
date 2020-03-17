# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->conftest.py
2020/3/9 14:08
@Desc:
"""
import pytest

#不带参数默认scope=function
@pytest.fixture()
def login():
    print ('登录，enter your username')

def test_s1(login):
    print ('case 1,登录后其他动作111')

def test_s2():
    print ('case2,不用登录，操作222')

def test_s3(login):
    print ('case 3,登录后333')

if __name__ == '__main__':
    pytest.main(['-s',''])