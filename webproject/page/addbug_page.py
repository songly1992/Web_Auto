#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
from common.base import Base
from page.login_page import LoginPage
import time
import os




# 切到ifrem上
locl_iframe = ("class name", "ke-edit-iframe")
timestr=time.strftime("%Y_%m_%d_%H_%M_%S")
test_title= u'BUG标题' + timestr
body = u'''【测试步骤】
              【实际结果】
              【预期结果】
       '''

class AddBugPage(Base):
    '''定位元素'''

    # 添加bug
    locl_test= ("link text", "测试")#测试
    locl_bug= ("link text", "Bug")  #BUG
    locl_add_bug = ("xpath", ".//*[@id='mainMenu']/div[3]/a[4]/i")#提bug
    locl_module=("css selector","#module_chosen > a.chosen-single.chosen-default > span")#所属模块
    locl_choose_module=("xpath","//li[@class='active-result highlighted']")#选择所属模块
    locl_proj = ("css selector","a.chosen-single.chosen-default > span")#所属项目
    locl_choose_proj=("xpath","//li[@class='active-result highlighted']")#选择所属项目
    locl_banben = ("class name", "chosen-choices")#影响版本
    locl_choose_banben = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li[1]") #选择影响版本
    locl_deadline=("id","deadline")  #截止日期
    locl_bug_tit1e = ("css selector", ".input-control.has-icon-right.required>input#title")#bug标题
    # 切到ifrem上
    locl_body = ("tag name", "body")
    #切回TOP Windows

    locl_addfile=("css selector","button.btn.btn-link.file-input-btn")#添加文件

    locl_save = ("xpath", ".//td/button[@id='submit']")

    # 新增列表标题
    locl_new = ("xpath", "//*[@id='bugList']/tbody/tr[1]/td[3]/a")
    locl_qr = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[3]/span")

    def click_test(self):
        '''点击测试栏'''
        self.click(self.locl_test)

    def click_bug(self):
        '''点击Bug'''
        self.click(self.locl_bug)

    def click_addbug(self):
        '''点击提bug'''
        self.click(self.locl_add_bug)

    def click_module(self):
        self.click(self.locl_module)
        self.click(self.locl_choose_module)

    def click_proj(self):
        self.click(self.locl_proj)
        self.click(self.locl_choose_proj)

    def click_banben(self):
        '''点击影响版本'''
        self.click(self.locl_banben)

    def click_choose_banben(self):
        self.click(self.locl_choose_banben)

    def sandkeys_deadline(self,dead):
        self.sendkeys(self.locl_deadline,dead)

    def sendkeys_bugtitle(self,title):
        '''输入bug标题'''
        self.sendkeys(self.locl_bug_tit1e,title)

    def sendkeys_body(self,body):
        '''输入重现步骤'''
        self.sendkeys(self.locl_body,body)

    def click_addfile(self):
        self.click(self.locl_addfile)

    def click_savebutton(self):
        '''点击保存按钮，提交bug'''
        self.click(self.locl_save)

    def is_add_bug_sucess(self,text):
        '''判断是否添加bug成功，添加成功返回新bug标题'''
        t=self.is_text_in_element(self.locl_new,text)
        return t

    def get_new_title(self):
        t=self.get_text(self.locl_new)
        return t
    def get_qr(self):
        t=self.get_text(self.locl_qr)
        return t

    def addbug(self):
        self.click_test()
        self.click_bug()
        self.click_addbug()
        self.click_module()
        self.click_banben()
        self.click_choose_banben()
        self.sandkeys_deadline("2018-12-30")
        self.sendkeys_bugtitle(test_title)
        self.to_iframe(locl_iframe)
        self.sendkeys_body(body)
        self.driver.switch_to.default_content()
        self.js_scroll_end()
        self.click_addfile()
        time.sleep(2)
        # 执行 autoit 上传文件
        file_path = r"C:\Users\Administrator\Pictures\timg.jpg"
        os.system(r"F:\github\Web_Auto\webproject\data\addfile.exe %s" % file_path)
        time.sleep(2)
        self.click_savebutton()

if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/biz/user-login.html")
    lg=LoginPage(driver)
    lg.login()
    print (u"登陆成功")
    bug=AddBugPage(driver)
    bug.addbug()
    result=bug.is_add_bug_sucess(test_title)
    print (result)
    a=bug.get_new_title()
    print (a)
    b=bug.get_qr()
    print (b)






