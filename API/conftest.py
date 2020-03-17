# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->conftest.py
2020/3/9 14:32
@Desc:
"""
import  pytest
@pytest.fixture(scope='module')
def login():
    print ('登录，enter your username')
    yield
    print ('登出。。。。。。')
def pytest_addoption(parser):
    parser.addoption('--cmdopt',action='store',default='type1',help='myoption:type1 or type2')

@pytest.fixture
def cmdopt(request):
    return request.config.getoption('--cmdopt')





