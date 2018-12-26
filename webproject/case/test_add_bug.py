#encoding=utf-8
#将默认编码设置为utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import unittest
from selenium import webdriver
from common.add_bug import add_bug
import time

class Test_Add_Bug(unittest.TestCase):

     @classmethod
     def setUpClass(cls):
         cls.driver=webdriver.Chrome()
         cls.driver.get("http://127.0.0.1/biz/user-login.html")
         cls.bug = add_bug(cls.driver)
         cls.bug.login()
         print ("登陆成功")

     def test_add_bug(self):
         timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
         test_title = u'BUG标题' + timestr
         self.bug.add_new_bug(test_title)
         result = self.bug.is_add_bug_sucess(test_title)
         print (result)
         self.assertTrue(result)

     @classmethod
     def tearDownClass(cls):
         cls.driver.quit()

if __name__=="__main__":
    unittest.main()

