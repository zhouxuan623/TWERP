# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_debug.py
2020/3/26 16:21
@Desc:
"""
# import pytest
# test_user_data = [('admin','11111'),{ "admin1",'22222'}]
#
# if __name__ == '__main__':
#     pytest.main(['-s','test_debug.py'])
results=['listing','fd']
envs = {'listing': "http://listing.tongtool.com/",
        'listing100': 'http://listing100.tongtool.com/',
        'listing-vip': 'http://listing-vip.tongtool.com/'}
hostnames = []
for result in results:
    hostname = envs.get(result)
    hostnames.append(hostname)

print (hostnames)

