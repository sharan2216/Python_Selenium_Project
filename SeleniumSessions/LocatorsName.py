from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://classic.freecrm.com')
driver.maximize_window()
driver.implicitly_wait(10)

username = driver.find_element(By.NAME,'username')
print("username found")
driver.implicitly_wait(3)

password = driver.find_element(By.NAME,'password')
print("password found")
driver.implicitly_wait(3)

login_Btn=driver.find_element(By.XPATH,"//input[@value='Login']")
username.send_keys("Admin")
password.send_keys("5r@1@YE@HPtu")
login_Btn.click()

driver.implicitly_wait(5)
title = driver.title
print("Title found")
print(title)



