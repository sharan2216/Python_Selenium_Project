import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import pytest


# @pytest.fixture(params=["chrome"], scope='class')
# def init_driver(request):
#     if request.param == "Chrome":
#         ch_driver = webdriver.Chrome()
#     # if request.param == "Firefox":
#     #     ff_driver = webdriver.Firefox()
#     request.cls.driver = webdriver
#     yield
#     webdriver.close()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
