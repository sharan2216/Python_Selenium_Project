from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://app.hubspot.com/login')
driver.maximize_window()
driver.implicitly_wait(5)

username = driver.find_element(By.CSS_SELECTOR,'#username')
password = driver.find_element(By.CLASS_NAME,'login-password')
login_Btn=driver.find_element(By.ID,'loginBtn')

act = ActionChains(driver)
act.send_keys_to_element(username ,'sksharan666@gmail.com' )
time.sleep(3)
act.send_keys_to_element(password ,'M4messi@fcb66')
time.sleep(3)
act.click(login_Btn).perform()

time.sleep(5)
title = driver.title
print("Title found")
print(title)

time.sleep(5)
