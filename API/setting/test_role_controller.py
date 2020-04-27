# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_role_controller.py
2020/4/27 11:19
@Desc:角色管理
"""
import pytest
from API.common import *
from faker import Factory

fake = Factory.create()


class Test_role_controller():
    def test_role_add(self, _headers, _operId):
        '角色添加POST /role'
        data = {
            "operIdList": [
                _operId
            ],
            "roleName": fake.name()
        }
        response_result('/role', _headers, 'post', data)

    def test_role_edit(self, _headers,_operId,role_infos):
        '角色编辑 /role'
        value = role_infos
        data = {
                "operIdList": [_operId],
                "roleName": value['rolename'],
                "roleId": value['roleid']
            }
        response_result('/role',_headers,'put',data)

    def test_role_query(self,_headers):
        '查询列表POST /role/query'
        response_result('/role/query',_headers,'post')

    @pytest.mark.skip(reason='孙嘉说是外部接口，跳过不测试')
    def test_queryAllRolesByAppid(self):
        '用appid查询所有角色GET /role/queryAllRolesByAppid'
        header = {'Accept': 'application/json',
                  'appid': f'{APPID}'}
        param={'emial':'test@13.com'}

        home_page = requests.post(SYS_URL+'/role/queryAllRolesByAppid', headers=header, params=param)
        response = home_page.json()
        assert response['code'] == 0, response

    def test_role_delete(self,_headers,roleid_delete):
        '删除角色/role/{roleId}'
        response_result(f'/role/{roleid_delete}',_headers,'delete')

    def test_role_detail(self,_headers,role_infos):
        '角色详情GET /role/{roleId} '
        role_id=role_infos['roleid']
        response_result(f'/role/{role_id}',_headers,'get')


if __name__ == '__main__':
    pytest.main(['-s', 'test_role_controller.py::Test_role_controller::test_role_detail'])
