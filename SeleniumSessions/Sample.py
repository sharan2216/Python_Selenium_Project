from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

options=webdriver.ChromeOptions()
options.add_argument("--headless")

driver= webdriver.Chrome(options=options)
driver.get('https://www.reddit.com/')

S=lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Height'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot("new_screenshot.png")