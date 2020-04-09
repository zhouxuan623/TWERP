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

    def test_stockout_list(self,_headers):
        '缺货订单列表 /order/stockout/list'
        url = SYS_URL+'/order/stockout/list'
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
        check_result(url,_headers,data)

    def test_order_sync(self,_headers):
        '手工同步线上订单 /order/sync'
        url = SYS_URL+'/order/sync'
        home_page = requests.post(url=url, headers=_headers,)
        response = home_page.json()
        assert response['code'] == 0, response['code']

    def test_update(self,_headers):
        u'订单编辑(编辑商品信息) /order/update'
        url = SYS_URL +'/order/update'
        sql = f"""SELECT a.sale_order_id,b.goods_id FROM {B_DATABASE}.tb1_sale_orders a LEFT JOIN {B_DATABASE}.tb1_order_goods b on a.sale_order_id=b.sale_order_id
where a.order_status in (1,2) and a.merchant_id='{MERCHANT}' ORDER BY a.sales_time desc limit 1;"""
        c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
        if len(c_mysql.query(sql)) == 0:
            pytest.skip(msg='没有匹配的订单')  # 跳过此用例
        sale_order_id,goods_id = (c_mysql.query(sql))[0]
        data={
                "orderGoodsList": [{
                    "goodsId":goods_id,
                    "goodsNum": random.randint(1,10)
                }],
                "saleOrderId": sale_order_id
            }
        response_result(url,_headers,'put',data)
    def test_updateBeforeShipmentStatus(self,_headers):
        '退回可出货post /order/updateBeforeShipmentStatus'
        url=SYS_URL+'/order/updateBeforeShipmentStatus'
        sale_order_id=sale_id(4)
        data={"saleOrderIds":[sale_order_id]}
        response_result(url,_headers,data=data)

    def test_updateCheckedStatus(self,_headers):
        '退回新订单POST /order/updateCheckedStatus'
        url=SYS_URL+'/order/updateCheckedStatus'
        sale_order_id=other_sale_id('order_status in (2,3)')
        data={"saleOrderIds":[sale_order_id]}
        response_result(url,_headers,data=data)

    def test_updateCheckingStatus(self,_headers):
        '退回核对中 POST /order/updateCheckingStatus'
        url = SYS_URL + '/order/updateCheckedStatus'
        sale_order_id = other_sale_id('order_status in (1)')
        data = {"saleOrderIds": [sale_order_id]}
        response_result(url, _headers, data=data)

    def test_updateCheckingStatus(self,_headers):
        '变更为出货中 POST /order/updateOnShipmentStatus'
        url = SYS_URL + '/order/updateOnShipmentStatus'
        sale_order_id = other_sale_id('order_status in (3)')
        data = {"saleOrderIds": [sale_order_id]}
        response_result(url, _headers, data=data)

    def test_updateShippingInformation(self,_headers):
        '修改实际配送地址 PUT /order/updateShippingInformation'
        url = SYS_URL+'/order/updateShippingInformation'
        sale_order_id = other_sale_id('order_status in (1,2,3,4)')
        data = {
                "saleOrderId": sale_order_id,
                "city": None,
                "phone": "0916914268",
                "postcode": None,
                "realDeliveryMethodName": "",
                "sysDeliveryMethodCode": "ACS-HK|空運",
                "recipientAddress1": "测试地址11",
                "recipientAddress2": "中西區",
                "recipientCountry": "HK",
                "recipientName": "zhouxuan",
                "recipientState": None,
                "warehouseId": WAREHOUSE_ID
            }
        response_result(url, _headers,method='put', data=data)

    def test_updateShippingStatus(self,_headers):
        '变更为已出货POST /order/updateShippingStatus'
        ##变更为已出货和同步托运状态无关，所有的出货中的都可以变为已出货
        url = SYS_URL+'/order/updateShippingStatus'
        sale_order_id = other_sale_id('order_status in (4)')
        data = {"saleOrderIds": [sale_order_id]}
        response_result(url, _headers, data=data)

    def test_updateTrackingData(self,_headers):
        '自定义物流填写跟踪单号 POST /order/updateTrackingData'
        url = SYS_URL+'/order/updateTrackingData'
        data = {
            "saleOrderId": shippingyourself(),
            "trackingNumber": ''
        }
        response_result(url,_headers,data=data)






















def sale_id(order_status):
    sql = f"SELECT a.sale_order_id from {B_DATABASE}.tb1_sale_orders a where a.order_status='{order_status}' and merchant_id='{MERCHANT}' ORDER BY a.sales_time desc limit 1;"
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

def shippingyourself():
    '使用自定义物流的订单'
    sql = f"""SELECT a.sale_order_id from {B_DATABASE}.tb1_sale_orders a where a.real_delivery_method_code not in (
            "ACS-HK|空運",
            "NV-SIN|空運",
            "tw_711_pay",
            "tw_711_nopay",
            "tw_711_b2c_pay",
            "tw_711_b2c_nopay",
            "tw_fm_c2c_pay",
            "tw_fm_c2c_nopay",
            "tw_fm_b2c_pay",
            "tw_fm_b2c_nopay",
            "711_return_nopay",
            "NV-MY|空運"
            ) and merchant_id='{MERCHANT}' ORDER BY a.sales_time desc limit 1;"""
    c_mysql = mysql(B_HOST, B_USER, B_PASSWORD, B_DATABASE)
    if len(c_mysql.query(sql)) == 0:
        pytest.skip(msg='没有匹配的订单')  # 跳过此用例
    sale_order_id = (c_mysql.query(sql))[0][0]
    return sale_order_id










if __name__ == '__main__':
    pytest.main(['-v','test_order.py::Test_order::test_updateTrackingData'])