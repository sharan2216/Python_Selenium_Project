from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://londonfreelance.org/courses/frames/index.html')
driver.maximize_window()
driver.implicitly_wait(10)
#
# driver.switch_to.frame(2)

driver.switch_to.frame('main')


header_value = driver.find_element(By.CSS_SELECTOR,'body >h2').text
# time.sleep(3)
print(header_value)
# driver.switch_to.frame(header_value)
time.sleep(3)
driver.switch_to.default_content()

# driver.switch_to.parent_frame()