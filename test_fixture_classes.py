import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import pytest



@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver=webdriver.Chrome()
    request.cls.driver=ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver=webdriver.Firefox()
    request.cls.driver=ff_driver
    yield
    ff_driver.close()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title=="Google"

@pytest.mark.usefixtures("init_ff_driver")
class Base_Firefox_Test:
    pass

class Test_Google_Firefox(Base_Firefox_Test):
    def test_google_title_firefoxe(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title=="Google"
