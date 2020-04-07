# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_product.py
2020/4/7 16:07
@Desc:
"""
import pytest
from API.common import *
import json
from faker import Factory
fake = Factory.create()
fake.pydecimal()

class Test_product():
    def test_add(self, _headers,_supplier,_categroy_id):
        '商品新增POST /product/add'
        url = SYS_URL+'/product/add'
        data ={
                "hscode": "hscode",
                "brand": "brand",
                "imgUrl": "",
                "skuCode": fake.word(),
                "productName": fake.company(),
                "productEnName": fake.word(),
                "categoryId": _categroy_id,
                "declareName": fake.name(),
                "declarePrice": str(fake.pydecimal(left_digits=2,right_digits=1,min_value=2,max_value=20)),
                "weight": fake.random_digit(),
                "length": str(fake.pydecimal(left_digits=2,right_digits=1,min_value=5,max_value=20)),
                "width":str(fake.pydecimal(left_digits=2,right_digits=1,min_value=2,max_value=5)),
                "height": str(fake.pydecimal(left_digits=2,right_digits=1,min_value=2,max_value=3)),
                "isMulti": 0,
                "supplierList": [{
                    "supplierId": _supplier,
                    "purchasingDays": "10",
                    "isPrimary": 1
                }, {
                    "supplierId": "",
                    "purchasingDays": None,
                    "isPrimary": 0
                }, {
                    "supplierId": "",
                    "purchasingDays": None,
                    "isPrimary": 0
                }]
            }
        response_result(url,_headers,data=data)
    def test_batchelete(self,_headers):
        '删除商品POST /product/batchDelete'
        url = SYS_URL+'/product/batchDelete'
        sql = f"SELECT product_id from {B_DATABASE}.tb1_product a where  a.merchant_id='{MERCHANT}' ORDER BY a.created_time DESC; ;"
        c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
        if len(c_mysql.query(sql)) == 0:
            pytest.skip(msg='没有可删除的商品')  # 跳过此用例
        data = {
              "productIds": [
                  (c_mysql.query(sql))[0][0]
              ]
            }
        response_result(url,_headers,data=data)

if __name__ == '__main__':
    pytest.main(['-v','test_product.py::Test_product::test_batchelete'])
