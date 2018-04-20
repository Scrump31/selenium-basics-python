from selenium import webdriver
import pytest
from time import sleep
from pages.google import GoogleHome


@pytest.mark.usefixtures('setDriver')
class TestGoogle():
    def test_search(self, setDriver):
        google = GoogleHome(setDriver)
        google.openPage()
        google.searchFor('selenium')

        assert google.driver.title == 'selenium - Google Search'
        google.endTest()

    @pytest.mark.skip(reason="dont need to run right now")
    def test_search2(self, setDriver):
        google = GoogleHome(setDriver)
        google.openPage()
        google.searchFor('Skookum')

        assert google.driver.title == 'Skookum - Google Search'
        google.endTest()
