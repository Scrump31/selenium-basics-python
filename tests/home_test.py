import pytest
from time import sleep
from pages.home_page import HomePage


@pytest.mark.usefixtures('setDriver')
class TestHome():
    def test_open_homepage(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()

        assert home.driver.title == 'Skookum - Strategy, Design, Development'
        home.endTest()

    def test_clickLetsWorkTogether_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickLetsWorkTogetherBtn()

        assert home.pageTitle == 'Skookum - Contact'
        home.endTest()

    def test_clickGetToKnowUs_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickGetToKnowUsBtn()

        assert home.pageTitle == 'Skookum - About'
        home.endTest()
