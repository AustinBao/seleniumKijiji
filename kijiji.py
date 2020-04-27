from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.7\geckodriver.exe')

driver.get("https://www.kijiji.ca/")

driver.maximize_window()

element = driver.find_element_by_id("SearchKeyword")
element.click()

# Using readline()
file1 = open('keywords.txt', 'r')
count = 0

while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))

    # askuser = input("What do you need to buy today?")
    element.send_keys(line)
    element.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    wait = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "title")))
    driver.find_element_by_class_name("title").click()

    driver.find_element_by_class_name("title-2323565163")
    print(driver.title)

file1.close()


