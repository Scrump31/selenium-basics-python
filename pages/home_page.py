from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Locators
_letsWorkTogetherBtn = '.page-header__content [href="/contact"]'
_getToKnowUsBtn = '.intro__markdown [href="/about"]'
_viewServicesBtn = '.services__link'
_exploreTheCaseStudyPremierBtn = '[href="/case-study/premier"]'
_exploreTheCaseStudyLibraryBtn = '[href="/case-study/charlotte-library"]'
_exploreTheCaseStudyHighPointBtn = '[href="/case-study/high-point"]'

class HomePage(BasePage):
	def __init__(self, driver):
		super().__init__(driver)
	

	# Getter Methods
	def getLetsWorkTogetherBtn(self):
		return self.driver.find_element(By.CSS_SELECTOR, _letsWorkTogetherBtn)
	
	def getGetToKnowUsBtn(self):
		return self.driver.find_element(By.CSS_SELECTOR, _getToKnowUsBtn)

	def getViewServicesBtn(self):
		return self.driver.find_element(By.CSS_SELECTOR, _viewServicesBtn)

	def getExploreTheCaseStudyPremierBtn(self):
		return self.driver.find_element(By.CSS_SELECTOR, _exploreTheCaseStudyPremierBtn)
	
	def getExploreTheCaseStudyLibraryBtn(self):
		return self.driver.find_element(By.CSS_SELECTOR, _exploreTheCaseStudyLibraryBtn)
	
	def getExploreTheCaseStudyHighPointBtn(self):
		return self.driver.find_element(By.CSS_SELECTOR, _exploreTheCaseStudyHighPointBtn)


	# Action Methods	
	def clickLetsWorkTogetherBtn(self):
		self.getLetsWorkTogetherBtn().click()
		self.verifyPageUpdatedTo('contact')
    
	def clickGetToKnowUsBtn(self):
		self.getGetToKnowUsBtn().click()
		self.verifyPageUpdatedTo('about')

    
	def clickViewServicesBtn(self):
		self.getViewServicesBtn().click()
		self.verifyPageUpdatedTo('services')
    
	def clickExploreTheCaseStudyPremierBtn(self):
		self.getExploreTheCaseStudyPremierBtn().click()
		self.verifyPageUpdatedTo('premier')
    
	def clickExploreTheCaseStudyLibraryBtn(self):
		self.getExploreTheCaseStudyLibraryBtn().click()
		self.verifyPageUpdatedTo('library')
    
	def clickExploreTheCaseStudyHighPointBtn(self):
		self.getExploreTheCaseStudyHighPointBtn().click()
		self.verifyPageUpdatedTo('high-point')
