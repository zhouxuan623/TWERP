# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->conftest.py
2020/4/9 13:51
@Desc:
"""
import pytest
from API.common import *

@pytest.fixture(scope='function')
def _private_shipping_order():
    '找出未初始化的商品'
    sql=f"""SELECT a.goods_id from {B_DATABASE}.tb1_product_inventory a where a.inventory_id not in (SELECT DISTINCT(inventory_id)
             from {B_DATABASE}.tb1_inventory_log ) and a.merchant_id='{MERCHANT}' and warehouse_id='{WAREHOUSE_ID}';"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的商品')  # 跳过此用例
    goods_id = (c_mysql.query(sql))[0][0]
    return goods_id
