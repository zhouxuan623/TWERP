# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_controller.py
2020/4/27 16:32
@Desc:平台管理
"""
import pytest
from API.common import *

class Test_controller():
    def test_enableWarrantySetValue(self,_headers):
        "启用保固助手 POST /setting/enableWarrantySetValue"
        """
        @:param:value 1 启用 0 关闭
        """
        data = {"operatorType": 0, "value": 1}
        response_result('/setting/enableWarrantySetValue',_headers,'post',data)

    def test_getMerchantSettingEmail(self,_headers):
        '获取商户设置的邮箱信息GET /setting/getMerchantSettingEmail'
        response_result('/setting/getMerchantSettingEmail',_headers,'get')

    def test_getMerchantSettings(self,_headers):
        "获取商户全部设置信息 GET /setting/getMerchantSettings"
        response_result('/setting/getMerchantSettings',_headers,'get')

    def test_getSyncItemWarningInfo(self,_headers):
        "获取库存同步助手设置信息 GET /setting/getSyncItemWarningInfo"
        response_result('/setting/getSyncItemWarningInfo',_headers,'get')

    def test_inventorySetValue(self,_headers):
        "启用库存同步助手 POST /setting/inventorySetValue"
        """
        @:param operatorStatus 0 停用  1启用
        """
        data = {"operatorStatus":1,"settingValue":4}
        response_result('/setting/inventorySetValue',_headers,'post',data)

    def test_setWarrantyEmail(self,_headers):
        "設定保固通知E-mail模板 POST /setting/setWarrantyEmail"
        data = {
              "emailContent": faker.text(),
              "emailTitle": faker.first_name()
            }
        response_result('/setting/setWarrantyEmail',_headers,'post',data)

    def test_settingcode(self,_headers,setting_code):
        '获取商户设置信息 GET /setting/{settingCode}'
        response_result(f"/setting/{setting_code}",_headers,'get')
if __name__ == '__main__':
    pytest.main(['-s','test_controller.py::Test_controller::test_settingcode'])


