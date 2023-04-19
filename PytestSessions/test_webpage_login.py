import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager


def test_amazon():
    driver=webdriver.Chrome()
    driver.get('https://google.com')
    assert driver.title =='Google'
    driver.quit()

def test_facebook():
    driver=webdriver.Chrome()

    driver.get('https://facebook.com')
    title=driver.title
    print(title)
    assert driver.title == 'Facebook – log in or sign up'
    driver.quit()

def test_instagram():
    driver=webdriver.Chrome()

    driver.get('https://instagram.com')
    assert driver.title =='Instagram'
    driver.quit()

def test_rediff():
    driver=webdriver.Chrome()

    driver.get('https://rediff.com')
    assert driver.title =='Rediff.com: News | Rediffmail | Stock Quotes | Shopping'
    driver.quit()

