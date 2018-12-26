#encoding=utf-8
from selenium import webdriver
from common.base import Base
import time


class addbug_page(Base):
    '''定位元素'''

    # 添加bug
    locl_test = ("link text", "测试")
    locl_bug = ("link text", "Bug")
    locl_add_bug = ("xpath", ".//*[@id='mainMenu']/div[3]/a[4]/i")
    locl_banben = ("class name", "chosen-choices")
    locl_choose_banben = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li[3]")
    locl_bug_tit1e = ("css selector", ".input-control.has-icon-right.required>input#title")
    # 切到ifrem上
    locl_iframe = ("class name", "ke-edit-iframe")
    locl_body = ("tag name", "body")
    locl_save = ("xpath", ".//td/button[@id='submit']")

    # 新增列表
    locl_new = ("xpath", "//*[@id='bugList']/tbody/tr[1]/td[3]/a")

    def click_test(self):
        '''点击测试栏'''
        ele=self.findElement(self.locl_test)


    def click_bug(self):
        '''点击Bug'''
        self.click(self.locl_bug)

    def click_addbug(self):
        '''点击提bug'''
        self.click(self.locl_add_bug)

    def click_banben(self):
        '''点击影响版本'''
        self.click(self.locl_banben)

    def click_choose_banebn(self):
        '''点击选择版本'''
        self.click(self.locl_choose_banben)

    def sendkeys_bugtitle(self,title):
        '''输入bug标题'''
        self.sendkeys(self.locl_bug_tit1e,title)


    def sendkeys_body(self,body):
        '''输入重现步骤'''
        self.sendkeys(self.locl_body,body)

    def click_savebutton(self):
        '''点击保存按钮，提交bug'''
        self.click(self.locl_save)

    def get_bug_newtitle(self):
        '''判断是否添加bug成功，添加成功返回新bug标题'''
        try:
            t=self.is_text_in_element(self.locl_new)
            return t
        except:
            return ""









