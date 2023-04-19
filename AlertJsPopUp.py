from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.NAME,'proceed').click()
time.sleep(3)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()

# alert.dismiss()
# alert .send_keys('hi)
driver.switch_to.default_content()
time.sleep(3)