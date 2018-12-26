#encoding=utf-8
#将默认编码设置为utf-8
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


from selenium import webdriver
from common.base import Base
import time


class add_bug(Base):   #继承Base类，就不用实例化

    '''定位元素'''
    locl_username=("id","account")      #登陆用户名
    locl_password=("name","password")   #登陆密码
    locl_subit=("id","submit")          #登陆提交
    #添加bug
    locl_test=("link text","测试")
    locl_bug=("link text","Bug")
    locl_add_bug=("xpath",".//*[@id='mainMenu']/div[3]/a[4]/i")
    locl_box=("class name","chosen-choices")
    locl_choose_box=("xpath",".//*[@id='openedBuild_chosen']/div/ul/li[3]")
    locl_bug_tit1e=("css selector",".input-control.has-icon-right.required>input#title")
    #切到ifrem上
    locl_iframe=("class name","ke-edit-iframe")
    locl_body=("tag name","body")
    locl_save=("xpath",".//td/button[@id='submit']")

    #新增列表
    locl_new=("xpath","//*[@id='bugList']/tbody/tr[1]/td[3]/a")

    def login(self):
       '''点击登陆'''
       # self.driver.get("http://127.0.0.1/biz/user-login.html")
       time.sleep(2)
       self.sendkeys(self.locl_username,"admin")
       self.sendkeys(self.locl_password,"sly1992.")
       self.click(self.locl_subit)

    def add_new_bug(self,test_title):
        '''添加bug'''
        self.click(self.locl_test)
        self.click(self.locl_bug)
        self.click(self.locl_add_bug)
        self.click(self.locl_box)
        self.click(self.locl_choose_box)
        # self.click(self.locl_bug_tit1e)
        self.sendkeys(self.locl_bug_tit1e,test_title)
        #切换到iframe
        iframe=self.findElement(self.locl_iframe)
        self.driver.switch_to_frame(iframe)
        txt=u'''【测试步骤】
               【实际结果】
               【预期结果】
        '''
        self.sendkeys(self.locl_body,txt)
        #切到当前也页面
        self.driver.switch_to.default_content()
        #滚动到底部
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.js_scroll_end()
        self.click(self.locl_save)

    def is_add_bug_sucess(self,text):
        return self.is_text_in_element(self.locl_new,text)


if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("http://127.0.0.1/biz/user-login.html")
    bug=add_bug(driver)
    bug.login()
    print ("登陆成功")
    timestr=time.strftime("%Y_%m_%d_%H_%M_%S")
    test_title= u'BUG标题' + timestr
    bug.add_new_bug(test_title)
    result=bug.is_add_bug_sucess(test_title)
    print (result)






