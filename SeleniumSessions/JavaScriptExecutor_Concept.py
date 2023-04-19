import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.amazon.in/')
driver.maximize_window()

BestSellers = driver.find_element(By.LINK_TEXT,'Best Sellers')
# driver.execute_script("arguments[0].click();",BestSellers)
title=driver.execute_script("return document.title;")
print(title)
#red Border line----------------------------
driver.execute_script("arguments[0].style.border ='3px solid red'",BestSellers)

#ScreenShot--------------------------------
# driver.get_screenshot_as_file("borderss.png")

# driver.execute_script("history.go(0);")
# driver.execute_script("alert('hello naveen');")
# inner_text = driver.execute_script("return document.documentElement.innerText")
# print(len(inner_text))

#scroll at bottom of the page-----------
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight) ")
# driver.get_screenshot_as_file("footers_screenshot.png")

#Scroll for the specific element----------------
jp = driver.find_element(By.PARTIAL_LINK_TEXT,'Japan')
driver.execute_script("arguments[0].scrollIntoView(true);",jp)
time.sleep(3)
driver.execute_script("arguments[0].style.border = '3px solid red'",jp)
driver.get_screenshot_as_file('backtotop.png')
time.sleep(5)
