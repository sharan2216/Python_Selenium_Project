from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

# for ele in dropdown_list:
#     print(ele.text)


def mutiple_select(droplist,value):
    if not value[0]=='all':
        for ele in droplist:
            print(ele.text)
            for k in range(len(value)):
                if ele.text==value[k]:
                    ele.click()
                    break

    else:
        try:
            for ele in droplist:
                ele.click()

        except Exception as e:
            print(e)

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,'justAnInputBox').click()
time.sleep(2)


dropdown_list=driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
time.sleep(2)

# value_list=['all']
value_list=['choice 2']
value_list=['choice 3','choice 2 1','choice 6 1','choice 7']
mutiple_select(dropdown_list,value_list)
time.sleep(5)