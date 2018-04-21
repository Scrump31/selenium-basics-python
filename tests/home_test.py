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

    def test_clickViewService_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickViewServicesBtn()

        assert home.pageTitle == 'Skookum - Services'
        home.endTest()

    def test_ExploreTheCaseStudyPremier_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickExploreTheCaseStudyPremierBtn()

        assert home.pageTitle == 'Case Study - Premier Inc'
        home.endTest()

    def test_ExploreTheCaseStudyLibrary_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickExploreTheCaseStudyLibraryBtn()

        assert home.pageTitle == 'Case Study - Charlotte Mecklenburg Library'
        home.endTest()


