# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_06.py
2020/3/9 15:16
@Desc:
"""
import  time
import pytest

@pytest.fixture(scope='module',autouse=True)
def start(request):
    print ('\n------开始执行module--------')
    print ('module:{0}'.format(request.module.__name__))
    print ('--------启动浏览器---------')
    yield
    print ('---------测试结束')

@pytest.fixture(scope='function',autouse=True)
def open_home(request):
    print ('function:%s \n --回到首页-----' %request.function.__name__)

def test_a():
    print ('-----用例a执行')

class Test_aaa():
    def test_01(self):
        print ('--------用例1---------')
    def test_02(self):
        print ('--------用例2--------')

if __name__ == '__main__':
    pytest.main(['-s','test_06.py'])