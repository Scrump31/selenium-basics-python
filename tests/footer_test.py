import pytest
from pages.footer_page import Footer


@pytest.mark.usefixtures('setDriver')
class TestFooter():
    def test_careers_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_getCareers_Link()

        assert footer.pageTitle == 'Skookum - Careers'

    def test_openSource_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_getOpenSource_Link()

        assert footer.pageTitle == 'Skookum · GitHub'

    def test_privacyPolicy_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_getPrivacyPolicy_Link()

        assert footer.pageTitle == 'Skookum - Privacy Policy'

    def test_contactUs_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_ContactUs_Link()

        assert footer.pageTitle == 'Skookum - Contact'

    def test_facebook_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_Facebook_Link()

        assert footer.pageTitle == 'Skookum - Home | Facebook'

    def test_linkedIn_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_LinkedIn_Link()

        assert footer.pageTitle == 'Skookum | LinkedIn'

    def test_twitter_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_Twitter_Link()

        assert footer.pageTitle == 'Skookum (@Skookum) | Twitter'

    def test_dribbble_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_Dribbble_Link()

        assert footer.pageTitle == 'Skookum - Dribbble'

    def test_instagram_link(self, setDriver):
        footer = Footer(setDriver)
        footer.openPage()
        footer.click_Instagram_Link()

        assert footer.pageTitle == 'Skookum (@skookuminc) • Instagram photos and videos'
