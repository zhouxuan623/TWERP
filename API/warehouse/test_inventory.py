# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_inventory.py
2020/4/9 10:24
@Desc:
"""
import pytest
from API.common import *
from faker import Factory
from random import randint
fake = Factory.create()
fake.pydecimal()

class Test_inventory():
    def test_commodities_list(self,_headers):
        '查询组合商品库存 POST /inventory/commodities/list'
        url = SYS_URL+'/inventory/commodities/list'
        data = {
              "warehouseId": WAREHOUSE_ID
            }
        response_result(url,_headers,data=data)

    def test_initial(self,_headers,_private_shipping_order):
        '库存初始化 PUT /inventory/initial'
        url =SYS_URL+'/inventory/initial'
        data ={
              "inventoryInfo": [
                {
                  "defectiveQuantity": 0,
                  "goodsId": _private_shipping_order,
                  "qualifiedQuantity": randint(1,10),
                  "stockWarning": randint(1,10)
                }
              ],
              "warehouseId": WAREHOUSE_ID
            }
        response_result(url,_headers,'put',data)
    def test_list(self,_headers):
        '查询商品库存 POST /inventory/list'
        url = SYS_URL+'/inventory/list'
        data={'warehouseId':WAREHOUSE_ID}
        response_result(url,_headers,data=data)





if __name__ == '__main__':
    pytest.main(['-s','test_inventory.py::Test_inventory::test_list'])