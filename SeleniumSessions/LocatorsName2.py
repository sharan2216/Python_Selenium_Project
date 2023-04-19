from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://demo.guru99.com/test/newtours/register.php')
driver.maximize_window()
driver.implicitly_wait(5)

# ele_country = driver.find_element(By.NAME,'country')
list_options = driver.find_elements(By.XPATH, '//select[@name="country"]/option')
# print(ele_country.text)
# ele_country.click()

# def select_values(element,value):
#     select = Select(element)
#     select.select_by_visible_text(value)


def select_dd_values(dropdownlist,value):
    print(len(list_options))
    for ele in dropdownlist:
      print(ele.text)
      if ele.text== value:
        ele.click()
        break

# select_values(ele_country,'INDIA')
select_dd_values(list_options,'INDIA')

#using List collection-----------------------------
# select = Select(ele_country)
# country_list=select.options
# print(len(country_list))
# for i in  country_list:
#     print(i.text)
#     if(i.text=='INDIA'):
#         i.click()
#         break
#--------------------------------

#using dropdown without Select Class

# list_options = driver.find_elements(By.XPATH, '//select[@name="country"]/option')
# print(len(list_options))
# for i in  list_options:
#     print(i.text)
#     if (i.text=='INDIA'):
#         break



# print(select.is_multiple)
# select.select_by_visible_text('BAHAMAS')
# select.select_by_index(4)
# select.select_by_value('ESTONIA')
# select.select_by_value('search-alias=hpc')
# dd_value=select.select_by_value('search-alias=hpc')


time.sleep(5)


