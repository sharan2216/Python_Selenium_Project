import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager

import pytest

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "Chrome":
        ch_driver = webdriver.Chrome()
    if request.param == "Firefox":
        ff_driver = webdriver.Firefox()
    request.cls.driver = webdriver
    webdriver.implicitly_wait(10)
    yield
    webdriver.close()