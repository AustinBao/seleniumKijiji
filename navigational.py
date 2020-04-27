from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\chromedriver")

driver.get("https://calendar.google.com/calendar/r?pli=1")

print(driver.title)

driver.get("https://translate.google.com/")

time.sleep(5)
print(driver.title)

driver.back()

time.sleep(5)
print(driver.title)

driver.forward()

time.sleep(5)
print(driver.title)