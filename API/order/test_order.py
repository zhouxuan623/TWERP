# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_order.py
2020/3/24 10:24
@Desc:订单平台状态0 核对中 , 1 新订单（已付款待配货） ,2 配货后缺货，3 配货完成  4 出货中(等待出货) ，
5 已出货，8、待取消(平台标记取消，但用户未取消) 9 取消
是否已付款，0未付款 1 已付款
sync_status  同步状态:0-- 未同步  1 --同步失败  2 -- 同步中  3 --同步成功   9--取消同步
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

    def test_createLogisticOrders(self,_headers):
        '同步托运方状态'
        url=SYS_URL+'/order/createLogisticOrders'
        "订单状态为出货中"
        data={"saleOrderIds":[sale_id(4)]}
        check_result(url, _headers, data)

    def test_delivered_list(self,_headers):
        '已出货订单列表'
        url=SYS_URL+'/order/delivered/list'
        data={
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
        check_result(url, _headers, data)

    def test_order_detail(self,_headers):
        '订单详情查看'
        sql=f"SELECT a.sale_order_id from {B_DATABASE}.tb1_sale_orders a where a.order_status=0 and merchant_id='{MERCHANT}' ORDER BY a.sales_time desc limit 1;"
        c_mysql=mysql(B_HOST,B_USER,B_PASSWORD,B_DATABASE)
        if len(c_mysql.query(sql))==0:
            pytest.skip(msg='订单数据为空')
            c_mysql.close()
        sale_order_id = (c_mysql.query(sql))[0][0]
        c_mysql.close()
        url=SYS_URL+f'/order/details/{sale_order_id}'
        check_result(url, _headers)

    def test_getMenuCount(self,_headers):
        u'获取菜单中各模块的数量/order/getMenuCount'
        url=SYS_URL+'/order/getMenuCount'
        check_result(url, _headers)

    # @pytest.mark.parametrize('url',[SYS_URL + '/order/getOnShipment',SYS_URL + '/order/getOnShipment'])
    def test_order_getOnShipment(self,_headers):
        "出货中订单的配送方式数量查询/order/getOnShipment"
        url = SYS_URL + '/order/getOnShipment'
        check_result(url,_headers)

    def test_markPaid(self,_headers):
        u'标记已付款POST /order/markPaid'
        url=SYS_URL+'/order/markPaid'
        sql = f"SELECT a.sale_order_id from {B_DATABASE}.tb1_sale_orders a where a.is_paid=0 and merchant_id='{MERCHANT}' ORDER BY a.sales_time desc limit 1;"
        c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
        if len(c_mysql.query(sql))==0:
            pytest.skip(msg='没有订单可以标记为已付款')  #跳过此用例
        sale_order_id = (c_mysql.query(sql))[0][0]
        c_mysql.close()
        data={"saleOrderIds":[f"{sale_order_id}"],"paymentType":2}
        check_result(url,_headers,data)

    def test_onshippingment_list(self,_headers):
        "出货中订单列表/order/onShipment/list"
        url=SYS_URL+'/order/onShipment/list'
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
        check_result(url,_headers,data)

    def test_pickingChecking(self,_headers):
        '新订单配货 /order/pickingChecked'
        url = SYS_URL+'/order/pickingChecked'
        data = {"saleOrderIds":[sale_id(1)]}
        check_result(url,_headers,data)

    def test_picking_stockout(self,_headers):
        '缺货订单配货/order/pickingStockout'
        url = SYS_URL+"/order/pickingStockout"
        data = {"saleOrderIds": [sale_id(2)]}
        check_result(url, _headers, data)

    def test_printLabelList(self,_headers):
        "打印出货标签 /order/printLabelList"
        url = SYS_URL+'/order/printLabelList'
        data = {
                  "saleOrderIds": [
                      other_sale_id('a.sync_status=3')
                  ]
        }
        check_result(url,_headers, data)

    def test_printPickingList(self,_headers):
        '打印拣货单'
        url = SYS_URL+'/order/printPickingList'
        data = {"saleOrderIds":[sale_id(4)]}
        check_result(url,_headers, data)

    def test_recheck(self,_headers):
        '重新核查订单/order/recheck'
        url = SYS_URL + '/order/recheck'
        data = {"saleOrderIds": [sale_id(0)]}
        check_result(url, _headers, data)






def sale_id(order_status):
    sql = f"SELECT a.sale_order_id from {B_DATABASE}.tb1_sale_orders a where a.is_paid='{order_status}' and merchant_id='{MERCHANT}' ORDER BY a.sales_time desc limit 1;"
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有匹配的订单')  # 跳过此用例
    sale_order_id = (c_mysql.query(sql))[0][0]
    return sale_order_id

def other_sale_id(sql_condition):
    sql = f"SELECT a.sale_order_id from {B_DATABASE}.tb1_sale_orders a where {sql_condition} and merchant_id='{MERCHANT}' ORDER BY a.sales_time desc limit 1;"
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有匹配的订单')  # 跳过此用例
    sale_order_id = (c_mysql.query(sql))[0][0]
    return sale_order_id







if __name__ == '__main__':
    pytest.main(['-v','test_order.py'])