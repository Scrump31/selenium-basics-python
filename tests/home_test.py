import pytest
from time import sleep
from pages.home_page import HomePage


@pytest.mark.usefixtures('setDriver', 'endTest')
class TestHome():
    def test_open_homepage(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()

        assert home.pageTitle == 'Skookum - Strategy, Design, Development'

    def test_clickLetsWorkTogether_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickLetsWorkTogetherBtn()

        assert home.pageTitle == 'Skookum - Contact'

    def test_clickGetToKnowUs_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickGetToKnowUsBtn()

        assert home.pageTitle == 'Skookum - About'

    def test_clickViewService_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickViewServicesBtn()

        assert home.pageTitle == 'Skookum - Services'

    def test_ExploreTheCaseStudyPremier_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickExploreTheCaseStudyPremierBtn()

        assert home.pageTitle == 'Case Study - Premier Inc'

    def test_ExploreTheCaseStudyLibrary_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickExploreTheCaseStudyLibraryBtn()

        assert home.pageTitle == 'Case Study - Charlotte Mecklenburg Library'

    def test_ExploreTheCaseStudyHighPoint_Btn(self, setDriver):
        home = HomePage(setDriver)
        home.openPage()
        home.clickExploreTheCaseStudyHighPointBtn()

        assert home.pageTitle == 'Case Study - High Point Market'
