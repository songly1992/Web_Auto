#encoding=utf-8

from selenium import webdriver
from page.addbug_page import AddBugPage
from page.login_page import LoginPage,login_url
from common.logger import Log
import unittest
import os
import time



class addbug_case(unittest.TestCase):

    log=Log()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(login_url)
        cls.lg = LoginPage(cls.driver)
        cls.lg.login()
        cls.log.info("登录成功")

    def test_001 (self):
        '''添加bug'''
        self.log.info("-----测试开始-----")
        self.bug = AddBugPage(self.driver)
        self.bug.click_test()
        self.bug.click_bug()
        self.bug.click_addbug()
        self.bug.click_module()
        self.bug.click_banben()
        self.bug.click_choose_banben()
        self.bug.sandkeys_deadline("2018-12-30")
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        test_title = u'BUG标题' + timestr
        self.bug.sendkeys_bugtitle(test_title)
        locl_iframe = ("class name", "ke-edit-iframe")
        self.bug.to_iframe(locl_iframe)
        body = u'''【测试步骤】
                      【实际结果】
                      【预期结果】
               '''
        self.bug.sendkeys_body(body)
        self.driver.switch_to.default_content()
        self.bug.js_scroll_end()
        self.bug.click_addfile()
        time.sleep(2)
        # 执行 autoit 上传文件
        file_path = r"C:\Users\Administrator\Pictures\timg.jpg"
        os.system(r"F:\github\Web_Auto\webproject\data\addfile.exe %s" % file_path)
        time.sleep(2)
        self.bug.click_savebutton()
        #判断是否添加成功
        result = self.bug.is_add_bug_sucess(test_title)
        print (result)
        self.log.info("---测试结束----")

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()#清除cookie，退出登录
        cls.driver.quit()


if __name__=="--main__":
    unittest.main()
