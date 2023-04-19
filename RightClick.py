from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
driver.implicitly_wait(5)

right_ele=driver.find_element(By.XPATH,"//span[text()='right click me']")
act=ActionChains(driver)
act.context_click(right_ele).perform()
time.sleep(3)

right_click_options=driver.find_elements(By.CSS_SELECTOR,'li.context-menu-icon span')
for ele in right_click_options:
    print(ele.text)
    if ele.text=='Copy':
        ele.click()
        break
time.sleep(3)