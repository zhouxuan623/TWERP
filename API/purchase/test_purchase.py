# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_purchase.py
2020/4/9 14:50
@Desc:
"""
import pytest
from API.common import *

class Test_purchase():
    def test_countByPurchaseStatus(self,_headers):
        '统计采购单状态数 POST /purchaseInfo/countByPurchaseStatus'
        url = SYS_URL+'/purchaseInfo/countByPurchaseStatus'
        data={"searchName":"","supplierId":"","purchaseStartTime":""}
        response_result(url,_headers,data=data)

    def test_create(self,_headers,_goods_id,_supplier):
        '新增采购单 POST /purchaseInfo/create'
        data = [
                  {
                    "purchaseDetailList": [
                      {
                        "goodsId": _goods_id,
                        "quantity": random.randint(1,10)
                      }
                    ],
                    "supplierId": _supplier,
                    "warehouseId": WAREHOUSE_ID
                  }
                ]
        response_result('/purchaseInfo/create',_headers,data=data)

    def test_delete_purchase(self,_headers,_purchase_id):
        '删除采购单 DELETE /purchaseInfo/delete/{purchaseId}'
        response_result(f'/purchaseInfo/delete/{_purchase_id(0)}',_headers,'delete')

    def test_forcecompleted(self,_headers,_purchase_id):
        '强制结案 PUT /purchaseInfo/forceCompleted'
        data={"purchaseId":_purchase_id(1)}
        home_page = requests.put(url=SYS_URL+'/purchaseInfo/forceCompleted', headers=_headers, params=data)
        response = home_page.json()
        assert response['code'] == 0, response

    def test_getSuppliers(self,_headers,_goods_id):
        '查询商品配置的所有供应商 GET /purchaseInfo/getSuppliers/{goodsId}'
        response_result(f"/purchaseInfo/getSuppliers/{_goods_id}",_headers,'get')

    def test_purchase_goods(self,_headers,_goods_id):
        '查看货品详细信息 POST /purchaseInfo/goods'
        """
        根据货品ID,获取货品对应的基本信息( 30天销量/60天销量... )
        """
        data={
              "goodsIds": [
                _goods_id
              ],
              "warehouseId": WAREHOUSE_ID
            }
        response_result('/purchaseInfo/goods',_headers,'post',data)

    def test_purchaseinfo_list(self,_headers,_supplier):
        '分页查询采购单 POST /purchaseInfo/list'
        data={
              "supplierId": WAREHOUSE_ID,
              "warehouseId": _supplier
            }
        response_result('/purchaseInfo/list',_headers,'post',data)

    def test_product_arrived_detail(self,_headers,_purchase_id):
        '根据采购单ID,查看采购单详细 GET /purchaseInfo/product/arrived/get/{purchaseId}'
        response_result(f"/purchaseInfo/product/arrived/get/{_purchase_id(2)}",_headers,'get')

    def test_product_arrived(self,_headers,_arriving):
        '收货 POST /purchaseInfo/productArrived'
        purchaseId,goodsId,qualifiedQuantity=_arriving
        data={
              "arrivalDetailList": [
                {
                  "defectiveQuantity": 0,
                  "goodsId": goodsId,
                  "qualifiedQuantity": qualifiedQuantity
                }
              ],
              "purchaseId": purchaseId
            }
        response_result('/purchaseInfo/productArrived',_headers,'post',data)

    def test_setting(self,_headers,_goods_id,_supplier):
        '商品叫货设定 POST /purchaseInfo/setting'
        data= [
                    {
                        "goodsId": _goods_id,
                        "supplierList": [
                            {
                                "isPrimary": 0,
                                "purchasingDays": 10,
                                "supplierId": _supplier
                            }
                        ]
                    }
                ]
        response_result('/purchaseInfo/setting',_headers,'post',data)

    def test_setting_list(self,_headers):
        '叫货清单列表查询 POST /purchaseInfo/setting/list'
        data={"pageNum":1,"pageSize":10,"searchName":""}
        response_result('/purchaseInfo/setting/list',_headers,'post',data)

    def test_getSupplierProduct(self,_headers,_stockingwarning):
        '根据厂商ID或叫货清单ID,生成预采购单 POST /purchaseInfo/stockwarning/getSupplierProduct'
        stock_warning_id,supplier_id,warehouse_id = _stockingwarning
        data={"supplierId":supplier_id,"searchName":"","stockWarningIds":[stock_warning_id],"warehosueId":warehouse_id}
        response_result('/purchaseInfo/stockwarning/getSupplierProduct',_headers,data=data)

    def test_stockwarning_list(self,_headers):
        '叫货清单分页查询 POST /purchaseInfo/stockwarning/list'
        data = {"pageNum":1,"pageSize":10,"searchName":"","supplierId":"","warehouseId":""}
        response_result('/purchaseInfo/stockwarning/list',_headers,data=data)

    def test_update(self,_headers,_purchase_id,_goods_id):
        '修改采购单 PUT /purchaseInfo/update'
        data={
                  "purchaseDetailList": [
                    {
                      "goodsId": _goods_id,
                      "quantity": 2
                    }
                  ],
                  "purchaseId": _purchase_id(0)
                }
        response_result('/purchaseInfo/update',_headers,'put',data)
















if __name__ == '__main__':
    pytest.main(['-vs','test_purchase.py::Test_purchase::test_update'])






