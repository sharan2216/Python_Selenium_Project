from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://app.hubspot.com/login')
driver.maximize_window()
driver.implicitly_wait(5)
# driver.find_element(By.CSS_SELECTOR,'#username').send_keys("sksharan666@gmail.com")
# # driver.find_element(By.CSS_SELECTOR,'input.form-control.private-form__control.login-email').send_keys("sksharan666@gmail.com")
# driver.find_element(By.XPATH,"//input[@class='form-control private-form__control login-email']").send_keys("sksharan666@gmail.com")
# # driver.find_element(By.CLASS_NAME,'login-email').send_keys("sksharan666@gmail.com")
# driver.find_element(By.CLASS_NAME,'login-password').send_keys("M4messi@fcb66")
# driver.find_element(By.CLASS_NAME,'login-submit').click()

# driver.find_element(By.LINK_TEXT,'Sign up').click()

driver.find_element(By.PARTIAL_LINK_TEXT,'Sign').click()
time.sleep(3)
title = driver.title
print("Title found")
print(title)