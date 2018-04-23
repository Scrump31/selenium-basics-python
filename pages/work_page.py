from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Locators
_premierInc_LearnMore_Link = '//h2[text()="Premier Inc: Technology That’s Transforming Healthcare"]'
_jri_Shocks_Link = '//h2[text()="JRi Shocks"]'
_metal_Marketing_Link = '//h2[text()="Metal Marketing"]'
_rj_Reynolds_Tobacco_Link = '//h2[text()="RJ Reynolds Tobacco"]'
_cola_Consolidated_Link = '//h2[text()="Coca-Cola Consolidated"]'
_electric_Power_Link = '//h2[text()="Electric Power Research Institute (EPRI)"]'
_adac_Automotive = '//h2[text()="ADAC Automotive"]'


class WorkPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Getter Methods

    def getPremierInc_LearnMore_Link(self):
        return self.driver.find_element(By.XPATH, _premierInc_LearnMore_Link)

    def getJri_Shocks_Link(self):
        return self.driver.find_element(By.XPATH, _jri_Shocks_Link)

    def getMetal_Marketing_Link(self):
        return self.driver.find_element(By.XPATH, _metal_Marketing_Link)

    def getRJ_Reynolds_Tobacco_Link(self):
        return self.driver.find_element(By.XPATH, _rj_Reynolds_Tobacco_Link)

    def getcola_Consolidated_Link(self):
        return self.driver.find_element(By.XPATH, _cola_Consolidated_Link)

    def getElectric_Power_Link(self):
        return self.driver.find_element(By.XPATH, _electric_Power_Link)

    def getAdac_Automotive_Link(self):
        return self.driver.find_element(By.XPATH, _adac_Automotive)

    # Action Methods
    def click_premierInc_LearnMore_Link(self):
        self.getPremierInc_LearnMore_Link().click()
        self.verifyPageUpdatedTo('premier')

    def click_Jri_Shocks_Link(self):
        self.getJri_Shocks_Link().click()
        self.verifyPageUpdatedTo('jri-shocks')

    def click_Metal_Marketing_Link(self):
        self.getMetal_Marketing_Link().click()
        self.verifyPageUpdatedTo('metal-marketing')

    def click_RJ_Reynolds_Tobacco_Link(self):
        self.getRJ_Reynolds_Tobacco_Link().click()
        self.verifyPageUpdatedTo('rj-reynolds')

    def click_cola_Consolidated_Link(self):
        self.getcola_Consolidated_Link().click()
        self.verifyPageUpdatedTo('coca-cola')

    def click_Electric_Power_Link(self):
        self.getElectric_Power_Link().click()
        self.verifyPageUpdatedTo('epri')

    def click_Adac_Automotive_Link(self):
        self.getAdac_Automotive_Link().click()
        self.verifyPageUpdatedTo('adac-automotive')
