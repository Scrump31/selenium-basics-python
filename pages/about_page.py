from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Locators
_our_story_button = 'a[href="/story"]'
_view_openings_button = '.about-cta__content [href="/careers"]'


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Getter Methods
    def getOurStory_Button(self):
        return self.driver.find_element(By.CSS_SELECTOR, _our_story_button)

    def getViewOpenings_Button(self):
        return self.driver.find_element(By.CSS_SELECTOR, _view_openings_button)

    # Action Methods
    def click_OurStory_Button(self):
        self.getOurStory_Button().click()
        self.verifyPageUpdatedTo('story')

    def click_ViewOpenings_Button(self):
        self.getViewOpenings_Button().click()
        self.verifyPageUpdatedTo('careers')
