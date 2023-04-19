from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.google.com/')
driver.maximize_window()
driver.implicitly_wait(3)

title=driver.title
print(title)