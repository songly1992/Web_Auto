#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
import unittest
from page.login_page import loginpage,login_url
import time


'''
1、输入admin，输入sly1992. 点击登录
2、输入admin，输入sly1992. 点击记住登录按钮，点击登录
3、输入admin,输入为空，点击登录
4、输入admin，输入123456，点击登录
5、输入admin22,输入123456，点击登录
'''


class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        cls.logintest=loginpage(cls.driver)

    def setUp(self):
        self.logintest.is_alert_exist()
        self.driver.get(login_url)
        self.driver.delete_all_cookies() #退出登录
        self.driver.refresh()

    def test_001(self):
        '''输入admin，输入sly1992. 点击登录'''
        self.logintest.input_username("admin")
        self.logintest.input_password("sly1992.")
        self.logintest.click_login_button()
        time.sleep(2)
        result=self.logintest.get_login_usernam()
        self.assertTrue(result=="admin")
        #断言

    def test_002(self):
        '''输入admin，输入sly1992. 点击记住登录按钮，点击登录'''
        self.logintest.input_username("admin")
        self.logintest.input_password("sly1992.")
        self.logintest.click_keeplogin()
        self.logintest.click_login_button()
        time.sleep(2)
        result = self.logintest.get_login_usernam()
        self.assertTrue(result == "admin")

    def test_003(self):
        '''输入admin,输入为空，点击登录'''
        self.logintest.input_username("admin")
        self.logintest.input_password("")
        self.logintest.click_login_button()
        time.sleep(2)
        result = self.logintest.get_login_usernam()
        self.assertTrue(result == "")

    def test_004(self):
        '''输入admin，输入123456，点击登录'''
        self.logintest.input_username("admin")
        self.logintest.input_password("123456")
        self.logintest.click_login_button()
        time.sleep(2)
        result = self.logintest.get_login_usernam()
        self.assertTrue(result == "")

    def test_005(self):
        '''输入admin22,输入123456，点击登录'''
        self.logintest.input_username("admin22")
        self.logintest.input_password("123456")
        self.logintest.click_login_button()
        time.sleep(2)
        result = self.logintest.get_login_usernam()
        self.assertTrue(result == "")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()