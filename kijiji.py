from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.7\geckodriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.kijiji.ca/")

element = driver.find_element_by_id("SearchKeyword")
element.click()
Askuser = input("What do you need to buy today?")
element.send_keys(Askuser)
element.send_keys(Keys.ENTER)


result = driver.find_element_by_class_name("title")
driver.implicitly_wait(200000)
result.click()

title = driver.find_element_by_class_name("title-2323565163")
print(title.text)

