# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test.py
2020/2/28 17:11
@Desc:
"""
def updateDict(paramdic,value):
    sm={}
    for key,value1 in paramdic.items():
        if key == "key":
            sm[key] = value
        else:
            sm[key] = value1
    return sm

if __name__ == '__main__':
    # print (aa())
    data={"key":'0000',"key1":"1111"}
    m=updateDict(data,"mmmm")
    n=updateDict(data,'nnnn')
    print(m,n)