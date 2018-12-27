#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from selenium import webdriver
import unittest
from page.login_page import loginpage,login_url
import time
import ddt
from common.read_excel import ExcelUtil

'''
1、输入admin，输入sly1992. 点击登录
2、输入admin，输入sly1992. 点击记住登录按钮，点击登录
3、输入admin,输入为空，点击登录
4、输入admin，输入123456，点击登录
5、输入admin22,输入123456，点击登录
'''
# datelist1=[{"user":"admin","pwd":"sly1992.","expect":"admin"},
#           {"user":"admin","pwd":" ","expect":""},
#           {"user":"admin","pwd":"123456","expect":""},
#           {"user":"admin22","pwd":"123456","expect":""}
#           ]
#
# datelist2=[{"user":"admin","pwd":"sly1992.","expect":"admin"},
#           {"user":"admin","pwd":" ","expect":""}
#           ]

'''测试数据'''
#数据文件路径
propath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath=os.path.join(propath,"data","logindata.xls")
print (filepath)

# filepath = "F:\\github\\Web_Auto\\webproject\\data\\logindata.xls"

sheetName1 = "Sheet1"
sheetName2 = "Sheet2"
data1 = ExcelUtil(filepath, sheetName1)
data2 = ExcelUtil(filepath, sheetName2)
datelist1=data1.dict_data()
datelist2=data2.dict_data()
print (datelist1)
print (datelist2)

@ddt.ddt
class Loginddt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        cls.logintest=loginpage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)

    def login_case1(self,user,pwd,expect):
        self.logintest.input_username(user)
        self.logintest.input_password(pwd)
        self.logintest.click_login_button()
        result=self.logintest.get_login_usernam()
        self.assertTrue(result==expect)

    def login_case2(self,user,pwd,expect):
        self.logintest.input_username(user)
        self.logintest.input_password(pwd)
        self.logintest.click_keeplogin()
        self.logintest.click_login_button()
        result=self.logintest.get_login_usernam()
        self.assertTrue(result==expect)

    @ddt.data(*datelist1)
    def test_001(self,data1):
        '''输入账号密码. 点击登录'''
        print ("--------------开始测试:test_001--------------")
        print ("测试数据:%s" % data1)
        self.login_case1(data1["user"],data1["pwd"],data1["expect"])
        print ("--------------结束测试:test_001--------------")

    @ddt.data(*datelist2)
    def test_002(self,data2):
        '''输入账号密码 点击记住登录按钮，点击登录'''
        print ("--------------开始测试：test_002--------------")
        print ("测试数据:%s" % data2)
        self.login_case2(data2["user"], data2["pwd"], data2["expect"])
        print ("--------------结束测试：test_002--------------")


    def tearDown(self):
        self.logintest.is_alert_exist()
        self.driver.delete_all_cookies()  # 退出登录
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()