from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.7\geckodriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.kijiji.ca/")
driver.implicitly_wait(20)

element = driver.find_element_by_id("SearchKeyword")
element.click()
element.send_keys("Guitar")
element.send_keys(Keys.ENTER)
driver.implicitly_wait(10000)

element = driver.find_element_by_class_name("title")
element.click()
driver.implicitly_wait(10000)

name = driver.find_element_by_class_name("title-2323565163")
print(name.text)