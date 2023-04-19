import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.implicitly_wait(10)
cookies = driver.get_cookies()
for cook in cookies:
    print(cook)
