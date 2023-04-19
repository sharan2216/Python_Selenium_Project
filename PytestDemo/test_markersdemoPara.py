import pytest
import sys


@pytest.mark.parametrize("username,password",
                         [
                           ("Selenium","Webdriver"),
                           ("Python","Pytest"),
                           ("Mukesh","Otwani"),

                         ]
                        )
def test_login(username,password):
    print(username)
    print(password)

