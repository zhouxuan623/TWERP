# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->conftest.py
2020/4/7 17:10
@Desc:
"""
import pytest
from API.common import *



@pytest.fixture(scope='module')
def _supplier():
    sql = f"SELECT supplier_id from twerp_db1.tb1_supplier where merchant_id='{MERCHANT}' and is_delete=0;"
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的供应商')  # 跳过此用例
    supplier_id = (c_mysql.query(sql))[0][0]
    return supplier_id

@pytest.fixture(scope='function')
def _categroy_id():
    "返回分类id 父类id"
    sql = f"SELECT category_id,category_name,parent_category_id from twerp_db1.tb1_product_category a where merchant_id='{MERCHANT}';"
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的分类')  # 跳过此用例
    category_id, category_name, parent_category_id= (c_mysql.query(sql))[0]
    return category_id,category_name,parent_category_id

@pytest.fixture(scope='function')
def _categroy_id_can_delete():
    sql = f"""SELECT category_id from {B_DATABASE}.tb1_product_category a where a.category_id not in (SELECT DISTINCT(category_id) from
 {B_DATABASE}.tb1_product a where a.merchant_id='{MERCHANT}')"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可删除的分类')  # 跳过此用例
    category_id = (c_mysql.query(sql))[0][0]
    return category_id

@pytest.fixture(scope='function')
def _product_id():
    sql = f"""SELECT product_id from {B_DATABASE}.tb1_product a where a.merchant_id='{MERCHANT}' ORDER BY created_time desc;"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的商品')  # 跳过此用例
    product_id = (c_mysql.query(sql))[0][0]
    return product_id


