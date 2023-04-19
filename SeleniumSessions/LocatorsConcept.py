from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager

# cPath = SeleniumManager.driver_location("chrome")
# print(cPath)
#
# fPath = SeleniumManager.driver_location("firefox")
# print(fPath)

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://shashi6666-osondemand.orangehrm.com/symfony/web/index.php/auth/login')
driver.implicitly_wait(3)

username = driver.find_element(By.ID,'txtUsername')
print("username found")
# username.click()
driver.implicitly_wait(3)
username.send_keys("Admin")
driver.implicitly_wait(3)

password = driver.find_element(By.ID,'txtPassword')
print("password found")
# password.click()
driver.implicitly_wait(3)
password.send_keys("5r@1@YE@HPtu")
driver.implicitly_wait(3)

login_button = driver.find_element(By.ID,'btnLogin')
print("login button found")
login_button.click()
driver.implicitly_wait(3)

title = driver.title
print("Title found")
print(title)