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

	# getViewServicesBtn(){
	# 	return this.driver.findElement(By.css(_viewServicesBtn));
	# }
	# getExploreTheCaseStudyPremierBtn(){
	# 	return this.driver.findElement(By.css(_exploreTheCaseStudyPremierBtn));
	# }
	# getExploreTheCaseStudyLibraryBtn(){
	# 	return this.driver.findElement(By.css(_exploreTheCaseStudyLibraryBtn));
	# }
	# getExploreTheCaseStudyHighPointBtn(){
	# 	return this.driver.findElement(By.css(_exploreTheCaseStudyHighPointBtn));
	# }

	# Action Methods	
	def clickLetsWorkTogetherBtn(self):
		self.getLetsWorkTogetherBtn().click()
		self.verifyPageUpdatedTo('contact')
    
	def clickGetToKnowUsBtn(self):
		self.getGetToKnowUsBtn().click()
		self.verifyPageUpdatedTo('about')

    
	# async clickViewServicesBtn() {
	# 	this.getViewServicesBtn().click();
	# 	await this.verifyPageUpdatedTo('services');
	# }
    
	# async clickExploreTheCaseStudyPremierBtn() {
	# 	this.getExploreTheCaseStudyPremierBtn().click();
	# 	await this.verifyPageUpdatedTo('premier');
	# }
    
	# async clickExploreTheCaseStudyLibraryBtn() {
	# 	this.getExploreTheCaseStudyLibraryBtn().click();
	# 	await this.verifyPageUpdatedTo('library');
	# }
    
	# async clickExploreTheCaseStudyHighPointBtn() {
	# 	this.getExploreTheCaseStudyHighPointBtn().click();
	# 	await this.verifyPageUpdatedTo('high-point');
	# }
