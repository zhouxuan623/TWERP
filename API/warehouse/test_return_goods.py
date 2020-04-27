# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_return_goods.py
2020/4/15 14:30
@Desc:退货return-goods-controller
"""
import pytest
from API.common import *

class Test_returnGoods():
    def test_returnGoods_exportExcel(self,_headers,_return_infos):
        '导出退货excel列表操作 POST /inventory/returnGoods/exportExcel'
        return_order_id, warehouse_id, sale_order_id, sale_account_id = _return_infos
        data = {
              "pageNum": 1,
              "pageSize": 10,
              "returnOrderIdList": [
                  return_order_id
              ],
              "saleAccountIdList": [
                  sale_account_id
              ],
              "searchName": "",
            }
        response_result('/inventory/returnGoods/exportExcel',_headers,data=data)

    def test_returngoods_list(self,_headers):
        '退货列表POST /inventory/returnGoods/list'
        data = {
              "pageNum": 1,
              "pageSize": 10,
              "returnOrderIdList": [
                ""
              ],
              "saleAccountIdList": [
                ""
              ],
            }
        response_result('/inventory/returnGoods/list',_headers,data=data)



if __name__ == '__main__':
    pytest.main(['-vs','test_return_goods.py::Test_returnGoods::test_returngoods_list'])



