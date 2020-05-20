
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Austi\Python\chromedriver")
# driver = webdriver.Firefox(executable_path=r'C:\Users\Austi\Python\geckodriver')

driver.get('https://www.youtube.com/')
driver.maximize_window()


