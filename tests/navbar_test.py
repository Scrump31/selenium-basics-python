import pytest
from pages.navbar_page import Navbar


@pytest.mark.usefixtures('setDriver', 'endTest')
class TestNavBar():
    def test_logo_link(self, setDriver):
        nav = Navbar(setDriver)
        nav.openPage()
        nav.click_logo_Link()

        assert nav.pageTitle == 'Skookum - Strategy, Design, Development'

    def test_services_link(self, setDriver):
        nav = Navbar(setDriver)
        nav.openPage()
        nav.click_services_Link()

        assert nav.pageTitle == 'Skookum - Services'

    def test_work_link(self, setDriver):
        nav = Navbar(setDriver)
        nav.openPage()
        nav.click_work_Link()

        assert nav.pageTitle == 'Our Work'

    def test_blog_link(self, setDriver):
        nav = Navbar(setDriver)
        nav.openPage()
        nav.click_blog_Link()

        assert nav.pageTitle == 'Our Blog'

    def test_events_link(self, setDriver):
        nav = Navbar(setDriver)
        nav.openPage()
        nav.click_events_Link()

        assert nav.pageTitle == 'Skookum - Events'

    def test_about_link(self, setDriver):
        nav = Navbar(setDriver)
        nav.openPage()
        nav.click_about_Link()

        assert nav.pageTitle == 'Skookum - About'

    def test_contact_link(self, setDriver):
        nav = Navbar(setDriver)
        nav.openPage()
        nav.click_contact_Link()

        assert nav.pageTitle == 'Skookum - Contact'
