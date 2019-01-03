#encoding=utf-8

from selenium import webdriver
from common.base import Base
from page.login_page import LoginPage,login_url
from page.addbug_page import AddBugPage
import time

class ConfirmBugPage(Base):

    # 定位元素
    locl_confirm=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[10]/a[1]/i") #确认bug
    locl_cs=("xpath",".//*[@id='mailto_chosen']/ul/li/input")#抄送给
    locl_choose_cs=("xpath",".//*[@id='mailto_chosen']/div/ul/li[3]")#选择抄送给谁
    #切换到iframe

    locl_body=("tag name","body")
    locl_save=("id","submit")#保存

    # 新增列表标题
    locl_new = ("xpath", "//*[@id='bugList']/tbody/tr[1]/td[3]/a")
    locl_qr=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[3]/span")
    def click_comfirm(self):
        self.click(self.locl_confirm)

    def click_cs(self):
        self.click(self.locl_cs)

    def click_choose_cs(self):
        self.click(self.locl_choose_cs)

    def sendkeys_body(self,text):
        # js_body ='document.getElementsByClassName("article-content")[0].valueOf=text'   #备注
        # self.driver.excute_script(js_body)
        self.sendkeys(self.locl_body,text)

    def click_save(self):
        self.click(self.locl_save)

    def get_new_title(self):
        t=self.get_text(self.locl_new)
        return t
    def is_secucss(self):
        t=self.is_text_in_element(self.locl_qr,u"[已确认]")
        return t

    def get_t(self):
        t=self.get_text(self.locl_qr)
        return t

    def confirmbug(self,text = u"备注哈哈哈哈哈哈哈"):
        self.click_comfirm()
        self.driver.switch_to.frame("iframe-triggerModal")
        self.click_cs()
        self.click_choose_cs()
        locl_iframe = ("class name", "ke-edit-iframe")
        self.to_iframe(locl_iframe)
        self.sendkeys_body(text)
        # js_body = 'document.getElementsByClassName("article-content")[0].value="99"'  # 备注
        # driver.execute_script(js_body)
        self.driver.switch_to.parent_frame()
        self.click_save()

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get(login_url)
    lg=LoginPage(driver)
    lg.login()
    print ("登录成功")
    ad=AddBugPage(driver)
    ad.addbug()
    cf=ConfirmBugPage(driver)
    cf.confirmbug()
    driver.refresh()
    time.sleep(1)
    #断言
    result=cf.is_secucss()
    print (result)
    qw=cf.get_t()
    print(qw)


    














