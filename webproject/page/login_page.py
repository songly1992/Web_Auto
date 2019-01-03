#encoding=utf-8
#将默认编码设置为utf-8
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


from selenium import webdriver
from common.base import Base
import time

login_url="http://127.0.0.1/biz/user-login.html"


class LoginPage(Base):   #继承Base类，就不用实例化

    '''定位登陆元素'''
    locl_username=("id","account")      #登陆用户名
    locl_password=("name","password")   #登陆密码
    locl_button=("id","submit")          #登陆提交
    locl_keeplogin=("id","keepLoginon")  #保存登陆勾选框
    locl_forgetpassword=("link text","忘记密码") #忘记密码
    locl_login_name=("css selector","#userNav>li>a") #登陆成功后的登录名
    login_url=("http://127.0.0.1/biz/user-login.html")

    def input_username(self,text):
        self.sendkeys(self.locl_username,text)

    def input_password(self,text):
        self.sendkeys(self.locl_password,text)

    def click_login_button(self):
        self.click(self.locl_button)

    def click_keeplogin(self):
        self.click(self.locl_keeplogin)

    def click_forgetpassword(self):
        self.click(self.locl_forgetpassword)


    def get_login_usernam(self):
        '''判断是否登陆成功，如果获取到admin返回t,如果获取不到返回空'''
        try:
            # t = self.driver.find_element_by_css_selector("#userNav>li>a").text
            t=self.get_text(self.locl_login_name)
            return t
        except:
            return ""

    def is_login_username(self,text):
             result=self.is_text_in_element(self.locl_login_name,text)
             return result


    def login(self,name="admin",pwd="sly1992.",keep_login=False):
       '''用户登陆'''
       self.driver.get(login_url)
       self.input_username(name)
       self.input_password(pwd)
       if keep_login:
           self.click_keeplogin() #若为Ture勾选，默认为False
       self.click_login_button()

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get(login_url)
    login_page=LoginPage(driver)
    login_page.input_username("admin")
    login_page.input_password("sly1992.")
    login_page.click_keeplogin()
    login_page.click_login_button()
