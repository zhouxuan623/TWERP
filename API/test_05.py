# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_05.py
2020/3/10 10:22
@Desc:
"""
import pytest

params=[{'user':'admin','pwd':''},{'user':'zhou','pwd':'dfd'}]
@pytest.fixture(scope='module')
def login(request):
    user = request.param['user']
    psw = request.param['pwd']
    print ('login account is {0},pwd is {1}'.format(user,psw))
    if psw:
        return True
    else:
        return False


@pytest.mark.parametrize('login',params,indirect=True)
class Test_xx():
    def test_01(self,login):
        'case1  login '
        result = login
        print ('case 1 {0}'.format(result))
        assert result==True

    def test_02(self,login):
        result = login
        print ('case2 result:{0}'.format(result))
        if not result:
            pytest.xfail('login fail ,marked xfail')
        assert  1==1

    def test_03(self,login):
        result = login
        print('case3 result:{0}'.format(result))
        if not result:
            pytest.xfail('login fail ,marked xfail')
        assert  1==1

if __name__ == '__main__':
    pytest.main(['-s','test_05.py'])


