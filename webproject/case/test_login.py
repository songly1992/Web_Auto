#coding=utf-8
from selenium import webdriver
from common.login_fction import login
from common.alert_exist import is_alert_exist
import select
import unittest
import time
#将默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class loginclass(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
     #启动浏览器并输入地址
     cls.driver = webdriver.Chrome()
     cls.driver.get("http://127.0.0.1/biz/user-login.html")
     time.sleep(2)
     print ('浏览器启动')

  def tearDown(self):
     is_alert_exist(self.driver)  # 调用is_alert_exist()方法
     #退出浏览器，清除cookies,然后刷新
     self.driver.delete_all_cookies()
     self.driver.refresh()

  @classmethod
  def tearDownClass(cls):
     #关闭浏览器
     cls.driver.quit()


  #判断是否登陆成功，如果获取到admin返回t,如果获取不到返回空
  def get_login_usernam(self):
     try:
         t = self.driver.find_element_by_css_selector("#userNav>li>a").text
         return t
     except:
         return ""


  def test_1(self):
     '''验证用户密码正确，登陆成功'''
     login(self.driver,"admin","sly1992.") #调用登陆函数


     #判断登陆结果
     t=self.get_login_usernam()   #调用获取登陆名的方法
     self.assertTrue(t == "admin")
     print ("登陆成功，获取登陆结果:"+t)

  def test_2(self):
     '''验证用户密码错误，登陆失败'''
     login(self.driver,"admin","123456")  #调用登陆函数


     #判断登陆结果
     t = self.get_login_usernam()  # 调用获取登陆名的方法
     print ("登陆失败，获取登陆结果："+t)
     self.assertTrue(t=="")




