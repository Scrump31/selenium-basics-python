from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# explicit wait libraries
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleHome():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    _search_field = '#lst-ib'

    # Getter Methods

    def getSearchField(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self._search_field)))

    # Action Methods
    def openPage(self):
        self.driver.get('http://www.google.com')

    def enterSearchTerm(self, searchterm):
        self.getSearchField().send_keys(searchterm)
        self.getSearchField().send_keys(Keys.ENTER)

    def submitSearch(self):
        return self.getSearchField().send_keys(Keys.ENTER)

    def searchFor(self, searchterm):
        self.enterSearchTerm(searchterm)
        self.submitSearch()
        self.wait.until(EC.url_contains(searchterm))

    def endTest(self):
        self.driver.quit()
