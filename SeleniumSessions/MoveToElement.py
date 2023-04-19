from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
driver.maximize_window()
driver.implicitly_wait(5)

source=driver.find_element(By.ID,'draggable')
target=driver.find_element(By.ID,'droppable')

act = ActionChains(driver)
# act.drag_and_drop(source,target).perform()
act.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(3)


