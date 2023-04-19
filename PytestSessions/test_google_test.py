import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import pytest


driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")


def teardown_module(module):
    driver.quit()


def test_Google_title():
    assert driver.title == "Google"


def test_Google_url():
    assert driver.current_url == "https://www.google.com/"
