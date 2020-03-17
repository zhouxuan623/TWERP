# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test_expectation.py
2020/3/9 16:13
@Desc:参数化
"""
import pytest
@pytest.mark.parametrize('test_input,expected',
                          [('3+5',8),('3+4',7),pytest.param('6*8',248,marks=pytest.mark.xfail),
                           ])
def test_eval(test_input,expected):
    assert eval(test_input)==expected


if __name__ == '__main__':
    pytest.main(['-s','test_expectation.py'])
