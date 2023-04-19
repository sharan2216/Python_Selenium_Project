import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC


def test_yatra():
    driver=webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    depart_from = driver.find_element(By.XPATH, '//input[@id="BE_flight_origin_city"]')
    # depart_from = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="BE_flight_origin_city"]')))
    depart_from.click()
    depart_from.send_keys("New Delhi")
    depart_from.send_keys(Keys.ENTER)

    going_to = driver.find_element(By.XPATH, '//*[@id="BE_flight_arrival_city"]')
    # going_to = wait.until(EC.element_to_be_clickable(By.XPATH, '//input[@id="BE_flight_arrival_city"]'))
    going_to.click()
    # time.sleep(3)
    going_to.send_keys("New York")
    going_to.send_keys(Keys.ENTER)
    time.sleep(3)
    search_flights_button = driver.find_element(By.XPATH,'//*[@id="BE_flight_origin_date"]')
    search_flights_button.click()
    time.sleep(6)
    # search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))
    # search_results.click()
    # # wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']")))
    # # all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']")))
    # all_dates = driver.find_element(By.XPATH, "//div[@id='monthWrapper']")
    # #
    # for date in all_dates:
    #     if date.get_attribute("data-date") == '22/05/2023':
    #      date.click()
    #      break
    # time.sleep(6)