from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
#'''screen shot for a page'''----------------------------
# driver.get_screenshot_as_file('reditt_1.png')

# width=1920
# height = driver.execute_script("return Math.max(document.body.scrollHeight,document.body.offsetHeight,document.documentElement.clientHeight,document.documentElement.scrollHeight,document.documentElement.offsetHeight);")

S =lambda X:driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('full_ss.png')

# driver.set_window_size(width,height)
# page_body = driver.find_element(By.TAG_NAME,'body')
# page_body.screenshot("full_page_screenshot.png")

