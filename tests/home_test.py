import pytest
from time import sleep
from pages.base_page import BasePage


@pytest.mark.usefixtures('setDriver')
class TestHome():
    def test_open_homepage(self, setDriver):
        home = BasePage(setDriver)
        home.openPage()

        assert home.driver.title == 'Skookum - Strategy, Design, Development'
        home.endTest()
