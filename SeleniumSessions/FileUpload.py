from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.NAME,'upfile').send_keys('D:/covid.txt')
driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(3)