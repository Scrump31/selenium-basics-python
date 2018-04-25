from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Locators
_careers_link = 'a.footer__link[href="/careers"]'
_open_source_link = 'a.footer__link[href="https://github.com/Skookum"]'
_privacy_policy_link = 'a.footer__link[href="/privacy"]'
_contact_us_link = 'a.footer__link[href="/contact"]'
_twitter_link = 'a.footer__link[href="https://twitter.com/skookum"]'
_facebook_link = 'a.footer__link[href="https://facebook.com/SkookumInc"]'
_linkedIn_link = 'a.footer__link[href="https://www.linkedin.com/company/skookum/"]'
_dribbble_link = 'a.footer__link[href="http://dribbble.com/skookum"]'
_instagram_link = 'a.footer__link[href="http://instagram.com/skookuminc"]'


class Footer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Getter Methods
    def getCareers_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _careers_link)

    def getOpen_source_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _open_source_link)

    def getPrivacy_policy_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _privacy_policy_link)

    def getContact_us_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _contact_us_link)

    def getFacebook_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _facebook_link)

    def getLinkedIn_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _linkedIn_link)

    def getTwitter_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _twitter_link)

    def getDribbble_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _dribbble_link)

    def getInstagram_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _instagram_link)

    # Action Methods
    def click_getCareers_Link(self):
        self.getCareers_link().click()
        self.verifyPageUpdatedTo('careers')

    def click_getOpenSource_Link(self):
        self.getOpen_source_link().click()
        self.verifyPageUpdatedTo('github')

    def click_getPrivacyPolicy_Link(self):
        self.getPrivacy_policy_link().click()
        self.verifyPageUpdatedTo('privacy')

    def click_ContactUs_Link(self):
        self.getContact_us_link().click()
        self.verifyPageUpdatedTo('contact')

    def click_Facebook_Link(self):
        self.getFacebook_link().click()
        self.verifyPageUpdatedTo('facebook')

    def click_LinkedIn_Link(self):
        self.getLinkedIn_link().click()
        self.verifyPageUpdatedTo('linkedin')

    def click_Twitter_Link(self):
        self.getTwitter_link().click()
        self.verifyPageUpdatedTo('twitter')

    def click_Dribbble_Link(self):
        self.getDribbble_link().click()
        self.verifyPageUpdatedTo('dribbble')

    def click_Instagram_Link(self):
        self.getInstagram_link().click()
        self.verifyPageUpdatedTo('instagram')
