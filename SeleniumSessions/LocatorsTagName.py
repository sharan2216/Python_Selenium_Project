from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.amazon.in')
driver.maximize_window()
driver.implicitly_wait(5)

# header_element=driver.find_element(By.TAG_NAME,'h1')
# linkslist=driver.find_elements(By.TAG_NAME,'a')
# print(len(linkslist))
#
# for ele in linkslist:
#     # print(ele.text)
#     print(ele.get_attribute('href'))

image_list = driver.find_elements(By.TAG_NAME,'img')
print(len(image_list))

for ele1 in image_list:
 # print(ele.text)
   print(ele1.get_attribute('src'))