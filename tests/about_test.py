import pytest
from pages.about_page import AboutPage


@pytest.mark.usefixtures('setDriver', 'endTest')
class TestAbout():
    def test_open_aboutpage(self, setDriver):
        about = AboutPage(setDriver)
        about.openPage('about')

        assert about.pageTitle == 'Skookum - About'

    def test_ourStory_Button(self, setDriver):
        about = AboutPage(setDriver)
        about.openPage('about')
        about.click_OurStory_Button()

        assert about.pageTitle == 'Skookum - Our Story'
        
    def test_viewOpenings_Button(self, setDriver):
        about = AboutPage(setDriver)
        about.openPage('about')
        about.click_ViewOpenings_Button()

        assert about.pageTitle == 'Skookum - Careers'
