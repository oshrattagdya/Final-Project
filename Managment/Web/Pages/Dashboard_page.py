from Managment.Web.Locators.Dashboard_locators import DashboardLocators
from selenium.webdriver.common.by import By


class DashboardPageFunc():
    def __init__(self, driver):
        self.driver = driver
        self.finnens = DashboardLocators.finnens
        self.cupons_button = DashboardLocators.cupons_button
        self.orders = DashboardLocators.orders
        self.products = DashboardLocators.products
        self.sells = DashboardLocators.sells
        self.stores = DashboardLocators.stores
        self.users = DashboardLocators.users

    def connect(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='טלפון']").send_keys('1950000000')
        self.driver.find_element(By.XPATH, "//input[@value='שלח לי קוד']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='קוד']").send_keys('1234')
        self.driver.find_element(By.XPATH, "//input[@value='כניסה']").click()

    def click_cup(self):
        self.driver.find_element(By.XPATH,self.cupons_button).click()

    def finnens(self):
        self.driver.find_element(By.XPATH,self.finnens).click()

    def orders(self):
        self.driver.find_element(By.XPATH,self.orders).click()



