#encoding=utf-8
from selenium import webdriver
from common.base import Base
from page.login_page import LoginPage,login_url
from page.addbug_page import AddBugPage
from page.confirmbug_page import ConfirmBugPage
from common.logger import Log
import time
import unittest

class confirmbug_case(unittest.TestCase):
    log=Log()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(login_url)
        cls.lg = LoginPage(cls.driver)
        cls.lg.login()
        cls.log.info ("登录成功")
        cls.ad = AddBugPage(cls.driver)
        cls.ad.addbug()
        cls.log.info ("添加bug成功")

    def test_001(self):
        '''确认bug'''
        self.log.info ("---测试开始----")
        self.cf = ConfirmBugPage(self.driver)
        self.cf.confirmbug()
        self.driver.refresh()
        time.sleep(1)
        # 断言
        result = self.cf.is_secucss()
        print (result)
        qw = self.cf.get_t()
        print(qw)
        self.log.info ("---测试结束----")

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.quit()

