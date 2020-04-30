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

@pytest.fixture(scope='function')
def saleaccount():
    '返回shopline卖家账号id和名称'
    sql = f"""SELECT a.sale_account_id,b.account,a.account_token,a.account_name,a.shopline_account_id from {B_DATABASE}.tb1_shopline_account a LEFT JOIN {B_DATABASE}.tb1_sale_account b on a.sale_account_id = b.sale_account_id where a.status=1
and a.merchant_id='{MERCHANT}';"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的信息')  # 跳过此用例
    sale_account_id,account,account_token,account_name,shopline_account_id = (c_mysql.query(sql))[0]
    return sale_account_id,account,account_token,account_name,shopline_account_id

@pytest.fixture(scope='function')
def carriername():
    "托运公司的"
    sql=f"""SELECT setting_code from {B_DATABASE}.tb1_merchant_settings a where a.setting_code like 'customerCode_%' and a.merchant_id='{MERCHANT}';"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的信息')  # 跳过此用例
    setting_codes = c_mysql.query(sql)
    carriernames=[]
    for setting_code in setting_codes:
        carriernames.append(setting_code[0].split('_',1)[1])
    return random.choice(carriernames)

@pytest.fixture(scope='function')
def sys_shipping():
    "common库中的实际托运方式"
    sql = f"""SELECT a.value_code from {C_DATABASE}.common_base_parameter a where a.parameter_name='logisticsType';"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的信息')  # 跳过此用例
    value_codes = c_mysql.query(sql)
    results=[]
    for value_code in value_codes:
        results.append(value_code[0])
    return random.choice(results)

@pytest.fixture(scope='function')
def delivery_mthod():
    "shopline有效账户下的托运方式id"
    sql = f"""SELECT a.delivery_method_id from {B_DATABASE}.tb1_delivery_method a LEFT JOIN {B_DATABASE}.tb1_shopline_account b on a.sale_account_id = b.sale_account_id 
where b.`status`=1 and a.merchant_id='{MERCHANT}';"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的信息')  # 跳过此用例
    delivery_method_ids = c_mysql.query(sql)
    results = []
    for delivery_method_id in delivery_method_ids:
        results.append(delivery_method_id[0])
    return random.choice(results)






