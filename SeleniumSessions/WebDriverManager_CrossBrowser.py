from selenium import webdriver
from selenium.webdriver.common.by import By

import time


browserName = "chrome"
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print("please pass the correct browser name" + browserName)

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID,'username').sendkeys("sksharan666@gmail.com")
driver.find_element(By.ID,'password').sendkeys("M4messi@fcb66")
driver.find_element(By.ID,'loginBtn').click()

time.sleep(4)

driver.quit()
