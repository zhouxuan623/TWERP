# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->generate_order.py
2020/2/27 14:45
@Desc:到shopline网站生成订单
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import  random

dr=webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(10)
def login():
    dr.get("https://admin.shoplineapp.com/admin/derek123587")
    dr.find_element_by_xpath("//input[@id='staff_email']").send_keys("wangyisong@tongtool.com")
    dr.find_element_by_xpath("//input[@id='staff_password']").send_keys("1qaz@WSX")
    dr.find_element_by_xpath('//*[@id="new_staff"]/div/button').click()
    "是否有消息tips"
    try:
        "切换到iframe下面"
        # dr.switch_to.frame(dr.find_elements_by_tag_name("iframe")[0])
        WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath("//iframe[@id='beamerNews']").is_displayed())

        dr.switch_to.frame(dr.find_element_by_xpath("//iframe[@id='beamerNews']"))
        WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath("/html/body/div/div[1]/div[3]").is_displayed())
        dr.find_element_by_xpath("/html/body/div/div[1]/div[3]").click()
        dr.switch_to.default_content()
        b=1
    except:
        b=2
        pass
    print ('b: ',b)
def order():
    WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath("//span[text()='訂單管理']").is_displayed())
    "判断进入的是设置页面还是订单处理界面"
    # try:
    #     WebDriverWait(dr, 10).until(lambda x: x.find_element_by_xpath('//span[@color="SNOW_100"][text()="SHOPLINE.bakery"]').is_displayed()) #订单处理界面
    #     b=1
    # except:
    #     b=2
    # print ('now b is',b)
    # if b==2:
    #     "设置为订单处理界面"
    #     time.sleep(3)
    #     dr.find_element_by_xpath('//span[@color="SNOW_100"]').click()
    #     dr.find_element_by_xpath("//span[@color='INK_600'][text()='CustHand']").click()
    dr.find_element_by_xpath("//span[text()='訂單管理']").click()
    time.sleep(2)
    dr.find_element_by_xpath("//span[text()='訂單']").click()

def create_order():
    WebDriverWait(dr, 15).until(lambda x: x.find_element_by_xpath('//*[@id="common-orders"]//orders-more-actions/ul/li/a').is_displayed())
    dr.find_element_by_xpath('//*[@id="common-orders"]//orders-more-actions/ul/li/a').click()
    dr.find_element_by_xpath('//*[@id="common-orders"]//orders-more-actions/ul/li/ul/li[1]/a').click()
    "客户资料"
    WebDriverWait(dr, 15).until(lambda x: x.find_element_by_xpath("//button[text()='選取顧客']").is_displayed())
    dr.find_element_by_xpath("//button[text()='選取顧客']").click()
    time.sleep(2)
    dr.find_element_by_xpath("//input[@placeholder='輸入顧客名字，手機號碼或電郵']").send_keys('zhouxuan',Keys.ENTER)
    time.sleep(5)
    WebDriverWait(dr, 15).until(lambda x: x.find_element_by_xpath("//input[@type='radio'][@name='selectedUser']").is_displayed())

    dr.find_element_by_xpath("//input[@type='radio'][@name='selectedUser']").click()
    dr.find_element_by_xpath("//div/button[2][text()='確定']").click()
    time.sleep(3)
    dr.find_element_by_xpath("(//button[text()='下一步'])[1]").click()
    "新增普通商品"
    time.sleep(3)
    dr.find_element_by_xpath('//button[@ng-click="openProductPicker()"]').click()
    WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath("//div[1][@ng-repeat='product in results track by product._id']/div/div[2]").is_displayed())
    time.sleep(2)
    dr.find_element_by_xpath("//div[1][@ng-repeat='product in results track by product._id']/div/div[2]").click()
    dr.find_element_by_xpath("//button[text()='保存']").click()
    time.sleep(3)
    dr.find_element_by_xpath("//button[@ng-click='prodcutSubmit()']").click()

    "新增商品,固定商品为多规格的apple"
    # time.sleep(3)
    # dr.find_element_by_xpath('//button[@ng-click="openProductPicker()"]').click()
    # WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath("//div[1][@ng-repeat='product in results track by product._id']/div/div[2]").is_displayed())
    # time.sleep(2)
    # dr.find_element_by_xpath("//input[@placeholder='輸入商品關鍵字或商品編號']").send_keys('Apple',Keys.ENTER)
    # time.sleep(3)
    # WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath("//div[1][@ng-repeat='product in results track by product._id']/div/div[2]").is_displayed())
    # dr.find_element_by_xpath("//div[1][@ng-repeat='product in results track by product._id']/div/div[2]").click()
    # dr.find_element_by_xpath("//button[text()='保存']").click()
    # time.sleep(3)
    # "规格"
    # dr.find_element_by_xpath("//order-form-product//order-subtotal-item/div/div[1]/div[1]/div[1]/div/select").click()
    # specfication_param=random.randint(1,3)
    # if specfication_param==1:
    #     dr.find_element_by_xpath("//order-form-product//order-subtotal-item/div/div[1]/div[1]/div[1]/div/select").send_keys(Keys.DOWN,Keys.ENTER)
    # elif specfication_param==2:
    #     dr.find_element_by_xpath("//order-form-product//order-subtotal-item/div/div[1]/div[1]/div[1]/div/select").send_keys(Keys.DOWN,Keys.DOWN,Keys.ENTER)
    # else:
    #     dr.find_element_by_xpath("//order-form-product//order-subtotal-item/div/div[1]/div[1]/div[1]/div/select").send_keys(Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.ENTER)
    # time.sleep(3)
    # dr.find_element_by_xpath("//button[@ng-click='prodcutSubmit()']").click()


    "送货资料 默认香港"
    time.sleep(3)
    dr.find_element_by_xpath("//div/order-form-delivery/div[2]/div[2]/div[1]/div[3]/select").click()
    dr.find_element_by_xpath("//div/order-form-delivery/div[2]/div[2]/div[1]/div[3]/select").send_keys(Keys.DOWN,Keys.ENTER)
    dr.find_element_by_xpath("//input[@ng-change='onSameAsCustomerChange()']").click()
    time.sleep(3)
    "地址"
    dr.find_element_by_xpath("//select[@ng-change='regionChange()']").click()
    dr.find_element_by_xpath("//select[@ng-change='regionChange()']").send_keys(Keys.DOWN,Keys.ENTER)
    dr.find_element_by_xpath("//select[@name='address2']").click()
    dr.find_element_by_xpath("//select[@name='address2']").send_keys(Keys.DOWN, Keys.ENTER)
    dr.find_element_by_xpath("//input[@name='address']").send_keys("测试地址1")
    dr.find_element_by_xpath("//button[@ng-click='deliverySubmit()']").click()
    time.sleep(2)
    "付款资料"
    dr.find_element_by_xpath("//select[@ng-model='$parent.payment']").click()
    dr.find_element_by_xpath("//select[@ng-model='$parent.payment']").send_keys(Keys.DOWN,Keys.ENTER)
    "确定"
    dr.find_element_by_xpath("//button[@ng-click='confirm()']").click()
    time.sleep(5)










if __name__ == '__main__':
    while 1:
        try:
            login()
            login_status = 1
        except:
            login_status = 2
            dr.close()
        if login_status==1:
            break
    while 1:
        try:
            order()
            order_menu=1
        except:
            order_menu=2
            dr.refresh()
            time.sleep(3)
        if order_menu==1:
            break
    value=100
    while value>0:
        try:
            create_order()
            print ('create success')
        except:
            dr.refresh()
            time.sleep(5)
        try:
            "进入创建界面，继续创建订单"
            WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath("//span[text()='訂單管理'][@color]").is_displayed())
            dr.find_element_by_xpath("//span[text()='訂單管理'][@color]").click()
            time.sleep(2)
            WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath("//span[text()='訂單']").is_displayed())
            dr.find_element_by_xpath("//span[text()='訂單']").click()
        except:
            pass
        value-=1









