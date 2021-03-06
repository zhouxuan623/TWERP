# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->conftest.py
2020/3/9 14:32
@Desc:
"""
import  pytest
import  requests
import  os
# from .common import  mysql,SYS_URL
from .common import *
import json


global token
token=''
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://10.0.8.67:7777",
        help="my option: type1 or type2"
    )


@pytest.fixture(scope='module')
def login():
    print ('登录，enter your username')
    yield
    print ('登出。。。。。。')
# def pytest_addoption(parser):
#     parser.addoption('--cmdopt',action='store',default='type1',help='myoption:type1 or type2')

@pytest.fixture
def cmdopt(request):
    return request.config.getoption('--cmdopt')

@pytest.fixture(scope='session',autouse=True)
def get_token():
    d = mysql('10.0.8.67', 'root', '12345678', 'common', 3306, 'utf8')
    sql1 = """insert into common.passport_ticket (ticket, merchant_id , user_id , email, status, creation_time
    ,invalidate_time,remember_expire)
    values (
    	uuid()	, '000007' , '201112010000000193' , 'test',1,now(),DATE_ADD(now(),interval 1800 MINUTE) , 1800
    );"""
    d.insert(sql1)
    ticket = (d.query(
        "SELECT ticket from common.passport_ticket where merchant_id='000007' ORDER BY creation_time desc LIMIT 1;"))[
        0][0]
    d.close()
    # os.environ['host'] = request.config.getoption('--cmdhost')
    # yield os.environ['host']
    # print (os.environ['host'])
    url = os.path.join(SYS_URL,'auth',f'{ticket}').replace('\\','/')
    s=requests.get(url)
    token = s.json()['datas']['token']
    print (token)
    return token


@pytest.fixture(scope='session')
def _headers(get_token):
    token = get_token
    header={'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization':f'{token}'}
    yield header


@pytest.fixture(scope='function')
def _supplier():
    '获取供应商id'
    sql = f"""SELECT supplier_id from {B_DATABASE}.tb1_supplier where merchant_id='{MERCHANT}' and is_delete=0 ORDER BY created_time DESC;"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的商品')  # 跳过此用例
    supplier_id = (c_mysql.query(sql))[0][0]
    return supplier_id





@pytest.fixture(scope='module')
def login(request):
    user,psw = request.param
    print("登录账户：%s" % user)
    print("登录密码：%s" % psw)
    if psw:
        return True
    else:
        return False






