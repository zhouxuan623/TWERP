# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->conftest.py
2020/4/9 14:50
@Desc:
"""
import pytest
from API.common import *

@pytest.fixture(scope='function')
def _goods_id():
    '可采购的商品ID'
    sql = f"""SELECT goods_id from {B_DATABASE}.tb1_goods a where a.merchant_id='{MERCHANT}' ORDER BY created_time desc;"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的商品')  # 跳过此用例
    goods_id = (c_mysql.query(sql))[0][0]
    return goods_id

@pytest.fixture(scope='function')
def _purchase_id():
    '可删除的采购单id '
    """
    @:param purchase_status  0 已生成待收货 1 部分收货(未结案) 2 已结案
    """
    def _purchase(status):
        sql = f"""SELECT a.purchase_id  from {B_DATABASE}.tb1_purchase_order a where a.purchase_status={status} and merchant_id='{MERCHANT}' ORDER BY created_time DESC;"""
        c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
        if len(c_mysql.query(sql)) == 0:
            pytest.skip(msg='没有可用的商品')  # 跳过此用例
        purchase_id = (c_mysql.query(sql))[0][0]
        return purchase_id
    return _purchase

@pytest.fixture(scope='function')
def _arriving():
    sql = f"""SELECT a.purchase_id,b.goods_id,b.quantity from {B_DATABASE}.tb1_purchase_order a LEFT JOIN {B_DATABASE}.tb1_purchase_order_detail b on
     a.purchase_id=b.purchase_id where a.merchant_id='{MERCHANT}' and a.purchase_status=0 ORDER BY a.created_time	DESC;"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有可用的数据')  # 跳过此用例
    arriving_info = (c_mysql.query(sql))[0]
    return arriving_info

