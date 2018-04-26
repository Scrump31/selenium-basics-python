from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Locators
_logo_home_link = 'a[href="/"]'
_services_link = '.main-nav a[href="/services"]'
_work_link = '.main-nav a[href="/work"]'
_blog_link = '.main-nav a[href="/blog"]'
_events_link = '.main-nav a[href="/events"]'
_about_link = '.main-nav a[href="/about"]'
_contact_link = '.main-nav a[href="/contact"]'


class Navbar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Getter Methods
    def getLogo_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _logo_home_link)

    def getServices_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _services_link)

    def getWork_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _work_link)

    def getBlog_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _blog_link)

    def getEvents_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _events_link)

    def getAbout_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _about_link)

    def getContact_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, _contact_link)

    # Action Methods
    def click_logo_Link(self):
        self.getLogo_link().click()
        self.verifyPageUpdatedTo('skookum')

    def click_services_Link(self):
        self.getServices_link().click()
        self.verifyPageUpdatedTo('services')

    def click_work_Link(self):
        self.getWork_link().click()
        self.verifyPageUpdatedTo('work')

    def click_blog_Link(self):
        self.getBlog_link().click()
        self.verifyPageUpdatedTo('blog')

    def click_events_Link(self):
        self.getEvents_link().click()
        self.verifyPageUpdatedTo('events')

    def click_about_Link(self):
        self.getAbout_link().click()
        self.verifyPageUpdatedTo('about')

    def click_contact_Link(self):
        self.getContact_link().click()
        self.verifyPageUpdatedTo('contact')
        