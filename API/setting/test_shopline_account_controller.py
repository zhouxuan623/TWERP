# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_shopline_account_controller.py
2020/4/28 14:09
@Desc:shopline-account-controller : shopline平台帐号管理
"""
import pytest
from API.common import *


class Test_shooline_controller():
    @pytest.mark.skip(reason='孙嘉说是外部调用的，swagger写的有问题')
    def test_updatestatus(self, _headers):
        "更新店铺状态(原始订单中心如果token失效回调次接口) PUT /shoplineAccount/api/updateStatus"
        data = {
            "merchantId": MERCHANT,
            "saleAccountId": "324340910961721344",
            "status": 0
        }
        pass

    def test_saleaccount_detail(self,_headers,saleaccount):
        saleAccountId = saleaccount[0]
        "获取账号详细 GET /shoplineAccount/detail/{saleAccountId}"
        response_result(f'/shoplineAccount/detail/{saleAccountId}',_headers,'get')

    def test_getCarriersWithDetail(self,_headers):
        "查询托运公司-托运方式GET /shoplineAccount/getCarriersWithDetail"
        response_result('/shoplineAccount/getCarriersWithDetail',_headers,'get')

    def test_getShippingMehtods(self,_headers,saleaccount):
        "根据店铺id获取运输方式GET /shoplineAccount/getShippingMehtods/{saleAccountId}"
        saleAccountId = saleaccount[0]
        response_result(f'/shoplineAccount/getShippingMehtods/{saleAccountId}',_headers,'get')
    @pytest.mark.skip(reason='先不实现，后续补充')
    def test_shoplineaccount_add(self,_headers):
        "添加删除shopline账号 POST /shoplineAccount/insert"
        data = {
                  "account": "string",
                  "accountCode": "string",
                  "accountName": "string",
                  "accountToken": "string",
                  "logo": "string",
                  "merchantId": "string",
                  "platformId": "string",
                  "shoplineStatus": 0,
                  "status": 0,
                  "userInfoIdList": [
                    "string"
                  ]
                }

    def test_insertCarrier(self,_headers):
        '新增自定义托运公司 POST /shoplineAccount/insertCarrier'
        data={ "carrierName": faker.company()}
        response_result('/shoplineAccount/insertCarrier',_headers,'post',data)

    def test_insertShippingMethod(self,_headers):
        "新增自定义托运方式 POST /shoplineAccount/insertShippingMethod"
        data = {
                  "carrierName": faker.name(),
                  "deliveryMethod": faker.country_code(),
                  "deliveryMethodCode": faker.country_code()
                }
        response_result('/shoplineAccount/insertShippingMethod',_headers,'post',data)

    def test_list(self,_headers):
        '分页查询帐户列表POST /shoplineAccount/list'
        data = {
                  "pageNum": 1,
                  "pageSize": 10,
                  "searchName": ""
                }
        response_result('/shoplineAccount/list',_headers,'post',data)
    def test_alllist(self,_headers):
        '查询所有账户列表GET /shoplineAccount/listAll '
        response_result('/shoplineAccount/listAll',_headers,'get')

    def test_listAllDeliveryMethods(self,_headers):
        'shopline获取所有物流方式 GET /shoplineAccount/listAllDeliveryMethods'
        response_result('/shoplineAccount/listAllDeliveryMethods',_headers,'get')

    def test_listAllPaymentMethods(self,_headers):
        'shopline获取所有付款方式 GET /shoplineAccount/listAllPaymentMethods'
        response_result("/shoplineAccount/listAllPaymentMethods",_headers,'get')

    def test_listSiteCode(self,_headers):
        "获取acs所有仓库代码 GET /shoplineAccount/listSiteCode"
        response_result('/shoplineAccount/listSiteCode',_headers,'get')

    def test_saveCustomerToken(self,_headers,carriername):
        "运输方式扩展方式保存 POST /shoplineAccount/saveCustomerToken"
        data = {
                  "carrierName": carriername,
                  "customerCode": faker.country_code(),
                  "isCustomizeCarrier": 0,
                  "senderAddress": faker.address(),
                  "senderCity": faker.city(),
                  "senderCountry": faker.country(),
                  "senderName": faker.name(),
                  "senderPhone": faker.phone_number(),
                  "senderProvince": faker.country_code(),
                  "siteCode": faker.country_code(),
                  "trackingUrl": faker.url()
                }
        response_result('/shoplineAccount/saveCustomerToken',_headers,'post',data)

    def test_syncDeliveryPaymentMethod(self,_headers,saleaccount):
        "shopline同步物流方式&付款方式 GET /shoplineAccount/syncDeliveryPaymentMethod/{shoplineAccountId}"
        shoplineAccountId=saleaccount[0]
        response_result(f'/shoplineAccount/syncDeliveryPaymentMethod/{shoplineAccountId}',_headers,'get')

    def test_shoplineAccount_update(self,_headers,saleaccount):
        "更新shopline账号 PUT /shoplineAccount/update"
        sale_account_id, account, account_token, account_name, shopline_account_id=saleaccount
        data = {
                  "account": account,
                  "accountName": account_name,
                  "accountToken": account_token,
                  "downloadOrder": 0,
                  "logo": "",
                  "saleAccountId": sale_account_id,
                  "shoplineAccountId": shopline_account_id,
                  "shoplineStatus": 1,
                  "status": 1,
                  "synDelivery": 0,
                  "userInfoIdList": []
                }
        response_result('/shoplineAccount/update',_headers,'put',data)

    def test_shoplineAccount_updateCarrier(self,_headers,carriername):
        "更新自定义托运公司 POST /shoplineAccount/updateCarrier"
        data = {
                  "carrierName": faker.name(),
                  "carrierOldName": carriername
                }
        response_result('/shoplineAccount/updateCarrier',_headers,'post',data)


    def test_updateCodCurrency(self,_headers):
        "更新托运方式cod币种&汇率 POST /shoplineAccount/updateCodCurrency "
        data = {
                  "carrierName": "ACS",
                  "codCurrency": "ARP",
                  "codRate": 0.5,
                  "deliveryMethodCode": "NV-SIN|空運"
                }
        response_result('/shoplineAccount/updateCodCurrency',_headers,'post',data)

    def test_updateRealShippingMethod(self,_headers,delivery_mthod,sys_shipping):
        "修改实际托运方式 POST /shoplineAccount/updateRealShippingMethod"
        data = {
                  "deliveryMethodId": delivery_mthod,
                  "sysDeliveryMethodCode": sys_shipping
                }
        response_result('/shoplineAccount/updateRealShippingMethod',_headers,'post',data)













if __name__ == '__main__':
    pytest.main(['-s','test_shopline_account_controller.py::Test_shooline_controller::test_shoplineAccount_updateCarrier'])