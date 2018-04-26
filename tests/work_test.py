import pytest
from time import sleep
from pages.work_page import WorkPage


@pytest.mark.usefixtures('setDriver', 'endTest')
class TestWork():
    def test_open_workpage(self, setDriver):
        work = WorkPage(setDriver)
        work.openPage('work')

        assert work.pageTitle == 'Our Work'

    def test_premierInc_learnMore_link(self, setDriver):
        work = WorkPage(setDriver)
        work.openPage('work')
        work.click_premierInc_LearnMore_Link()

        assert work.pageTitle == 'Case Study - Premier Inc'

    def test_JRi_Shocks_link(self, setDriver):
        work = WorkPage(setDriver)
        work.openPage('work')
        work.click_Jri_Shocks_Link()

        assert work.pageTitle == 'Case Study - JRi Shocks'

    def test_metal_marketing_link(self, setDriver):
        work = WorkPage(setDriver)
        work.openPage('work')
        work.click_Metal_Marketing_Link()

        assert work.pageTitle == 'Case Study - Metal Marketing'

    def test_rj_reynolds_link(self, setDriver):
        work = WorkPage(setDriver)
        work.openPage('work')
        work.click_RJ_Reynolds_Tobacco_Link()

        assert work.pageTitle == 'Case Study - RJ Reynolds Tobacco'

    def test_coca_cola_link(self, setDriver):
        work = WorkPage(setDriver)
        work.openPage('work')
        work.click_cola_Consolidated_Link()

        assert work.pageTitle == 'Case Study - Coca-Cola Consolidated'

    def test_electric_power_link(self, setDriver):
        work = WorkPage(setDriver)
        work.openPage('work')
        work.click_Electric_Power_Link()

        assert work.pageTitle == 'Case Study - Electric Power Research Institute (EPRI)'

    def test_adac_automotive_link(self, setDriver):
        work = WorkPage(setDriver)
        work.openPage('work')
        work.click_Adac_Automotive_Link()

        assert work.pageTitle == 'Case Study - ADAC Automotive'
