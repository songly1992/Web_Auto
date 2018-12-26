# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def login(driver,username,password):
    # driver.find_element_by_id("account").send_keys(username)
    # driver.find_element_by_name("password").send_keys(password)
    # driver.find_element_by_css_selector("#keepLoginon").click()
    # driver.find_element_by_id("submit").click()

    #另一种方法，快而稳的定位元素
    element1=WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id("account"))
    element1.send_keys(username)

    element2 =WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_name("password"))
    element2.send_keys(password)

    element3=WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id("submit"))
    element3.click()



