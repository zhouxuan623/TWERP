# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->conftest.py
2020/4/27 13:48
@Desc:
"""
import pytest
import random
from API.common import *

@pytest.fixture(scope='function')
def _operId():
    return random.choice(OPERIDS)

@pytest.fixture(scope='function')
def role_infos():
    sql = f"""SELECT a.role_id,a.role_name from {B_DATABASE}.tb1_role a LEFT JOIN {B_DATABASE}.tb1_role_oper b on a.role_id=b.role_id 
               where a.merchant_id='{MERCHANT}' ;"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的角色信息')  # 跳过此用例
    role_id,role_name = (c_mysql.query(sql))[0]
    result = {'roleid':role_id,'rolename':role_name}
    return result

@pytest.fixture(scope='function')
def roleid_delete():
    sql = f"""SELECT role_id  from {B_DATABASE}.tb1_role a where a.role_id not in (SELECT DISTINCT(role_id) from {C_DATABASE}.user_role) 
              and a.merchant_id='{MERCHANT}' ORDER BY a.created_time desc;"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的角色信息')  # 跳过此用例
    role_id = (c_mysql.query(sql))[0]
    return role_id[0]

@pytest.fixture(scope='function')
def setting_code():
    sql = f"""SELECT setting_code from {B_DATABASE}.tb1_merchant_settings a where a.merchant_id='{MERCHANT}' ORDER BY a.created_time desc;"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的信息')  # 跳过此用例

    setting_codes = (c_mysql.query(sql))
    results=[]
    for i in setting_codes:
        results.append(i[0])
    return random.choice(results)  #随机返回一个setting_code




