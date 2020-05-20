from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"CC:\Users\Austi\Python\chromedriver")

driver.get("http://newtours.demoaut.com/")

user_ele = driver.find_element_by_name("userName")
print(user_ele.is_displayed()) #returns true/false based on find element
print(user_ele.is_enabled())  #returns true/false

password_ele = driver.find_element_by_name("password")
print(password_ele.is_displayed())
print(password_ele.is_enabled())

user_ele.send_keys("mercury")
password_ele.send_keys("mercury")

driver.find_element_by_name("login").click()


roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")

roundtrip_radio.is_selected()