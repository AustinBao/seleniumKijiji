
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome(executable_path=r"C:\Users\chromedriver")
driver = webdriver.Firefox(executable_path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.7\geckodriver.exe')

driver.maximize_window()
driver.get("https://chrome.google.com/webstore/category/extensions")

driver.get(driver.title)
driver.get(driver.current_url)

