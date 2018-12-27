#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

class Base():
  def __init__(self,driver):
      self.driver=driver
      self.timeout=10 #总共查询多长时间
      self.t=0.5  #0.5秒查询一次

  def findElement(self,locator):
      if not isinstance(locator,tuple):
          print (u'locator参数类型错误，必须传元祖类型：locl=("id","account")')
      else:
          try:
             print (u"正在定位元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1]))
             ele=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
             return ele
          except:
              return ""



  #另一种判断元素方法
  def findElementNew(self,locator):
      '''定位到元素，返回元素，没有定位到元素，返回Timeout异常'''
      ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(*locator))
      return ele

  def select_by_index(self,locator,index=0):
      '''通过索引，index是索引第几个，从0开始，默认选择第一个'''
      ele=self.findElement(locator)
      Select(ele).select_by_index(index)

  def select_by_value(self,locator,value):
      '''通过value属性定位'''
      ele=self.findElement(locator)
      Select(ele).select_by_value(value)

  def select_by_text(self,locator,text):
      '''通过文本值定位'''
      ele=self.findElement(locator)
      Select(ele).select_by_visible_text(text)

  def get_text(self,locator):
      '''获取文本'''
      try:
          t=self.findElement(locator).text
          return t
      except:
          print ("获取text失败，返回''")
          return ""

  def get_name(self,locator,name):
      '''获取属性'''
      try:
          ele=self.findElement(locator)
          return ele.get_attribute(name)
      except:
          print("获取属性失败，返回''")
          return ""


  def is_title(self,title_name):
      '''判断当前页面的title，返回bool值'''
      result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title_name))
      return result

  def is_title_contains(self,title_name):
      '''判断当前页面的title是否包含预期字符串，返回布尔值'''
      result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title_name))
      return result

  def is_text_in_element(self,locator,text):
      '''判断某个元素中的text是否包含预期的字符串，返回布尔值'''
      try:
          result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,text))
          return result
      except:
          return False

  def is_value_in_element(self,locator,value):
      '''
      判断某个元素中的value属性是否包含预期的字符串,返回布尔值
      value为空，返回False
      :param locator:
      :param value:
      :return:
      '''
      try:
          result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, value))
          return result
      except:
          return False

  # def is_alter_exist(self):
  #     '''判断当前是否有alert弹出框'''
  #     try:
  #         result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
  #         return result
  #     except:
  #         return False

  def is_alert_exist(self):
      '''判断alert弹窗是不是存在'''
      try:
          time.sleep(2)
          alert = self.driver.switch_to.alert
          textname = alert.text
          alert.accept()  # 有alert,点击alert
      except:
          return ""

  def to_iframe(self,locator):
      '''切到iframe上'''
      ele = self.findElement(locator)
      self.driver.switch_to_frame(ele)

  def move_to_element(self,locator):
      '''鼠标悬停操作'''
      ele=self.findElement(locator)
      ActionChains(driver).move_to_element(ele).perform()

  def js_scroll_end(self):
      '''滚动到底部'''
      js_end="window.scrollTo(0, document.body.scrollHeight)"
      self.driver.execute_script(js_end)

  def js_terget(self,locator):
      '''聚焦元素'''
      terget=self.findElement(locator)
      self.driver.execute_script("arguments[0].scrollIntoView();",terget)

  def js_scroll_top(self):
      '''滚动到顶部'''
      js_top="window.scrollTo(0, 0)"
      self.driver.execute_script(js_top)



  # def sendkeys(self,loctor,text):
  #     ele=self.findElement(loctor)
  #     ele.send_keys(text)

  def sendkeys(self,loctor,text,is_clear_first=False):
      '''is_clear_first默认为False，不清空输入框'''
      ele=self.findElement(loctor)
      if is_clear_first:
          ele.clear()   #is_clear_first为Ture的时候执行
      ele.send_keys(text)

  def click(self,loctor):
      ele=self.findElement(loctor)
      ele.click()

if __name__=="__main__":
        driver=webdriver.Chrome()
        driver.get("http://127.0.0.1/biz/user-login.html")
        b1=Base(driver)
        local=("id","account")
        b1.sendkeys(local,"admin")
