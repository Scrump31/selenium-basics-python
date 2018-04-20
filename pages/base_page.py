from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selectors
_home = 'http://www.skookum.com'


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.pageTitle = None

    # Action Methods
    def openPage(self, url=_home):
        base = _home

        if url == 'home':
            url = base

        elif url == 'services':
            url = f'{base}/services'

        elif url == 'work':
            url = f'{base}/work'

        elif url == 'blog':
            url = f'{base}/blog'

        elif url == 'events':
            url = f'{base}/events'

        elif url == 'about':
            url = f'{base}/about'

        elif url == 'contact':
            url = f'{base}/contact'

        else:
            url = base

        self.driver.get(url)
        self.driver.maximize_window()
        self.pageTitle = self.getCurrentPageTitle()

    def verifyPageUpdatedTo(self, page):
        self.wait.until(EC.url_contains(page))
        self.pageTitle = self.getCurrentPageTitle()

    def getCurrentPageTitle(self):
        return self.driver.title

    def endTest(self):
        return self.driver.quit()
