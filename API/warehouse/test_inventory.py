# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->rest_inventory.py
2020/4/9 10:24
@Desc:
"""
import pytest
from API.common import *
from faker import Factory
fake = Factory.create()
fake.pydecimal()

class Test_inventory():
    def test_commodities_list(self,_headers):
        '查询组合商品库存 POST /inventory/commodities/list'
        url = SYS_URL+'/inventory/commodities/list'
        data =