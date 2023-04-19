from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="D:\\CHROME DRIVERS\\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
driver.find_element(By.NAME,'q').click()
driver.find_element(By.NAME,'q').send_keys("Naveen Automationlabs")

optionsListpip install webdriver-manager=driver.find_elements(By.CSS_SELECTOR,'ul.G43f7e li ')
print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text=='naveen automationlabs youtube':
        ele.click()
        break



time.sleep(5)

driver.quit()