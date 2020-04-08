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
                "categoryId": _categroy_id[0],
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
    def test_category_add(self,_headers):
        '新增商品分类POST /product/category/add'
        url = SYS_URL+'/product/category/add'
        data = {"categoryName":fake.word()}
        response_result(url,_headers,data=data)

    def test_category_delelte(self,_headers,_categroy_id_can_delete):
        '删除商品分类DELETE  /product/category/delete/{productCategoryId}'
        url = SYS_URL+f'/product/category/delete/{_categroy_id_can_delete}'
        response_result(url,_headers,method='delete')

    def test_category_list(self,_headers):
        '商品分类列表POST /product/category/list'
        url=SYS_URL+'/product/category/list'
        response_result(url,_headers)

    def test_category_update(self,_headers,_categroy_id):
        '修改商品分类PUT /product/category/update'
        url = SYS_URL+'/product/category/update'
        category_id,category_name, parent_category_id=_categroy_id
        data={
                "categoryName": category_name+fake.word(),
                "parentCategoryId": parent_category_id,
                "categoryId":category_id ,
                "displayOrder": -1
            }
        response_result(url,_headers,'put',data)

    def test_fuzzylookupgoods(self,_headers):
        '仅根据SKU选择货品 POST /product/fuzzyLookupGoods'
        url = SYS_URL+'/product/fuzzyLookupGoods'
        data = {
                  "pageNum": 1,
                  "pageSize": 10,
                  "searchName": "z"
                }
        response_result(url,_headers,data=data)

    def test_getProductDetail(self,_headers,_product_id):
        'GET /product/getProductDetail/{productId}'
        url = SYS_URL+f'/product/getProductDetail/{_product_id}'
        response_result(url,_headers,'get')

    def test_myProducts(self,_headers):
        '查询商品 POST /product/myProducts'
        url = SYS_URL+'/product/myProducts'
        data = {"pageSize":10,"pageNo":1,"searchName":"","categoryIds":[]}
        response_result(url,_headers,data=data)

    def test_selectGoods(self,_headers):
        '选择货品 POST /product/selectGoods'
        url = SYS_URL+'/product/selectGoods'
        data={
                  "pageNum": 1,
                  "pageSize": 10,
                  "searchName": "z"
                }
        response_result(url,_headers,data=data)

    def test_product_update(self,_headers,_product_info):
        '修改商品 PUT /product/update'
        url = SYS_URL+'/product/update'
        product_id, category_id, product_name, sku_code=_product_info
        data = {
                "productId": product_id,
                "categoryId": category_id,
                "skuCode": sku_code,
                "productName": product_name,
                "productEnName": fake.word(),
                "hscode": "",
                "brand": "",
                "weight": 0,
                "length": 0,
                "width": 0,
                "height": 0,
                "imageThumbUrl": None,
                "imgUrl": None,
                "declareName": "",
                "declarePrice": None,
                "declareCurrency": "USD",
                "isMulti": 0,
                "merchantId": MERCHANT,
                "mulitList": None,
                "supplierList": [{
                    "supplierId": "",
                    "purchasingDays": None,
                    "isPrimary": 0
                }, {
                    "supplierId": "",
                    "purchasingDays": None,
                    "isPrimary": 0
                }, {
                    "supplierId": "",
                    "purchasingDays": None,
                    "isPrimary": 0
                }],
                "deletedGoodsIds": []
            }
        response_result(url,_headers,'put',data)

    def test_updateproductcategory(self,_headers,_product_id,_categroy_id):
        '批量修改商品分类PUT /product/updateProductCategory '
        url = SYS_URL+'/product/updateProductCategory'
        data={
              "categoryId":_categroy_id[0] ,
              "productList": [
                  _product_id
              ]
            }
        response_result(url,_headers,'put',data)














if __name__ == '__main__':
    pytest.main(['-v','test_product.py::Test_product::test_updateproductcategory'])

