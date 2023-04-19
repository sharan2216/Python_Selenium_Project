from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time
options = webdriver.ChromeOptions()
options.headless = True
driver=webdriver.Chrome()
driver.implicitly_wait(10)


driver.get('https://www.amazon.in/')
print(driver.title)