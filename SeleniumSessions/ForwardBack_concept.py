import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[@class='nav-a nav-a-2   nav-progressive-attribute']").click()
driver.implicitly_wait(10)


time.sleep(3)
title = driver.title
print("1st Title found------")
print(title)

driver.back()
title = driver.title
print("2nd Title found------")
print(title)
driver.forward()
title = driver.title
print("3rd Title found------")
print(title)
time.sleep(3)
driver.back()
time.sleep(3)
