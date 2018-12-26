#encoding=utf-8
import time
def is_alert_exist(driver):
   '''判断alert弹窗是不是存在'''
   try:
       time.sleep(2)
       alert=driver.switch_to.alert
       textname=alert.text
       alert.accept() #有alert,点击alert
   except:
       return ""