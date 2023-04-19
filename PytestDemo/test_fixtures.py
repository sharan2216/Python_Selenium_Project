import time
import allure
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = None


@pytest.fixture
def setup():
    print("Start Browser")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()
    print("Close Browser")


@allure.description("Validates Google Login")
@allure.severity(severity_level="CRITICAL")
def test_1(setup):
    try:
        driver.get('https://google.com')
        print("Test1 executed")
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="Invalid data",
                          attachment_type=allure.attachment_type.PNG)


@allure.description("Validates facebook login")
@allure.severity(severity_level="NORMAl")
def test_2(setup):
    try:
        driver.get('https://facebook.com')
        driver.find_element(By.ID, "email").send_keys("sksharan666@gmail.com")
        time.sleep(5)
        driver.find_element(By.ID, "pass").send_keys("155113412")
        time.sleep(3)
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)
        print("Test2 executed")
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="Invalid data 2",
                          attachment_type=allure.attachment_type.PNG)


@allure.description("Validates insta Login")
@allure.severity(severity_level="LOW")
def test_3(setup):
    try:
        driver.get('https://instagram.com')
        time.sleep(3)
        print("Test3 executed")
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="Invalid data 3",
                          attachment_type=allure.attachment_type.PNG)
