import  time

import pytest
import time
from SeleniumSessions.ElementActionConcept import password


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestHubSpot(BaseTest):
    @pytest.mark.parametrize(
                                "username, password",
                                [
                                    ("sksharan666@gmail.com", "M4messi@fcb66"),
                                    ("naveen@gmail.com", "naveen123"),# this is sample credentials
                                ]
                            )
    def test_login(self, username, password):
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, "username").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID, "password").send_keys(password)

