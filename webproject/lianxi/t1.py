#encoding=utf-8
#将默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("http://127.0.0.1/biz/user-login.html")
loc2=(By.CSS_SELECTOR,".form-actions>a")
ww=Base(driver)
ww.findElement(loc2)
r1=ww.is_title("用户登录 - 禅道")
print (r1)
r2=ww.is_title_contains("禅道")
print (r2)
r3=ww.is_text_in_element(loc2,"忘记密码")
print (r3)
