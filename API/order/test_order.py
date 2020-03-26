# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_order.py
2020/3/24 10:24
@Desc:
"""
import requests
import pytest
from API.common import *
import json
class Test_order():
    def test_order_beforeshipment_list(self,_headers):
        "全局查找"
        url=SYS_URL+'/order/beforeShipment/list'
        data={"pageNum":1,
            "pageSize":10,
            "searchName":"",
            "accountId":"",
            "deliveryMethodId":"",
            "paymentMethodId":"",
            "warehouseId": ""}
        home_page=requests.post(url,headers=_headers,data=json.dumps(data))
        result = home_page.json()
        assert result['code']==0

    def test_order_cancel(self,_headers):
        "待核查的订单可取消"
        url = SYS_URL+'/order/cancel'
        T_mysql=mysql(B_HOST,B_USER,B_PASSWORD,B_DATABASE)
        sql=f"SELECT a.sale_order_id from {B_DATABASE}.tb1_sale_orders a where a.order_status=0 and merchant_id='{MERCHANT}' ORDER BY a.sales_time desc LIMIT 1;"
        T_result = (T_mysql.query(sql))[0][0]
        data={
              "deliveryMethodId": "",
              "isInBlackList": 0,
              "paymentMethodId": "",
              "paymentType": 0,
              "platformId": "",
              "refPlatformOrder": "",
              "saleOrderIds": [
                f"{T_result}"
              ],
              "searchName": ""
            }
        home_page = requests.post(url,headers=_headers,data=json.dumps(data))
        result = home_page.json()

    def test_order_checked_list(self,_headers):
        '新订单列表 /order/checked/list'
        url = SYS_URL+'/order/checked/list'
        data = {
                "pageNum": 1,
                "pageSize": 10,
                "searchName": "",
                "accountId": "",
                "deliveryMethodId": "",
                "paymentMethodId": "",
                "salesTimeEnd": "",
                "salesTimeStart": "",
                "isInBlackList": None
            }
        home_page = requests.post(url,headers=_headers,data=json.dumps(data))
        response = home_page.json()
        assert response['code']==0
    def test_checking_list(self,_headers):
        '核对中订单列表 /order/checking/list '
        url=SYS_URL+'/order/checking/list'
        data = {
                "pageNum": 1,
                "pageSize": 10,
                "searchName": "",
                "accountId": "",
                "deliveryMethodId": "",
                "paymentMethodId": "",
                "salesTimeEnd": "",
                "salesTimeStart": "",
                "isInBlackList": None
            }
        home_page = requests.post(url,headers=_headers,data=json.dumps(data))
        response = home_page.json()
        assert  response['code']==0,response['code']

    def test_order_getOnShipment(self,_headers):
        "出货中列表查询"
        url = SYS_URL + '/order/getOnShipment'
        home_page = requests.get(url, headers=_headers)
        response = home_page.json()
        assert response['code'] == 0




if __name__ == '__main__':
    pytest.main(['-s','test_order.py'])