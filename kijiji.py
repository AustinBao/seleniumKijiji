from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'C:\Users\Austi\Python\geckodriver')

driver.get("https://www.kijiji.ca/")

driver.maximize_window()

element = driver.find_element_by_id("SearchKeyword")
element.click()

Askuser = input("What do you need to buy today?")
element.send_keys(Askuser)
element.send_keys(Keys.ENTER)


wait = WebDriverWait(driver, 10)
wait = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "title")))
driver.find_element_by_class_name("title").click()


driver.find_element_by_class_name("title-2323565163")
print(driver.title)

driver.close()


