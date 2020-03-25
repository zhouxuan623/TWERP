# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->common.py
2020/3/23 10:51
@Desc: 参考https://www.jianshu.com/p/ab9477abc0a5
"""
from faker import Factory
import string
import random
import  pymysql


SYS_URL="http://10.0.8.67:7777"
MERCHANT = '000007'

"common顶级库"
C_HOST ='10.0.8.67'
C_USER ='root'
C_PASSWORD ='12345678'
C_DATABASE = 'common'
C_PORT = 3306

"67业务库"
B_HOST='10.0.8.67'
B_USER = 'ibizdata'
B_PASSWORD='123456'
B_DATABASE = 'twerp_db1'
B_PORT = 3306

class mysql():
    def __init__(self,host,user,password,database,port=3306,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.datebase = database
        self.port = port
        self.charset = charset
        self._conn = pymysql.connect(host=self.host,user=self.user,password=self.password,port=self.port,charset=self.charset)
        self._cursor = self._conn.cursor()
    def query(self,sql):
        "返回一个二维tuple"
        try:
            self._cursor.execute(sql)
            result = self._cursor.fetchall()
        except pymysql.Error as e:
            print (e)
            result = False
        return result
    def insert(self,sql):
        try:
            self._cursor.execute(sql)
            self._conn.commit()
            result =  True
        except pymysql.Error as e:
            print (e)
            result = False
        return result

    def close(self):
        self._cursor.close()
        self._conn.close()

if __name__ == '__main__':
    # conn = pymysql.connect(host='10.0.8.67', user='root', password='12345678', port=3306,
    #                         charset='utf8')
    # cursor = conn.cursor()
    # sql1="""insert into common.passport_ticket (ticket, merchant_id , user_id , email, status, creation_time
    # ,invalidate_time,remember_expire)
    # values (
    # 	uuid()	, '000007' , '201112010000000193' , 'test',1,now(),DATE_ADD(now(),interval 1800 MINUTE) , 1800
    # );"""
    # cursor.execute(sql1)
    # conn.commit()
    # cursor.close()
    # conn.close()

    d=mysql('10.0.8.67','root','12345678','common',3306,'utf8')
    sql1="""insert into common.passport_ticket (ticket, merchant_id , user_id , email, status, creation_time
,invalidate_time,remember_expire)
values (
	uuid()	, '000007' , '201112010000000193' , 'test',1,now(),DATE_ADD(now(),interval 1800 MINUTE) , 1800
);"""
    d.insert(sql1)
    ticket=(d.query("SELECT ticket from common.passport_ticket where merchant_id='000007' ORDER BY creation_time desc LIMIT 1;"))[0][0]
    print (ticket)
    d.close()







