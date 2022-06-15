import allure
from Managment.Web.Locators.Dashboard_locators import DashboardLocators
from selenium.webdriver.common.by import By
from Managment.Web.Utils.utils import Utilitis
from time import sleep




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
        self.allnav = DashboardLocators.allnav


    @allure.step
    def click_cup(self):
        self.driver.find_element(By.XPATH,self.cupons_button).click()

    @allure.step
    def finnens_click(self):
        self.driver.find_element(By.XPATH,self.finnens).click()

    @allure.step
    def orders_click(self):
        self.driver.find_element(By.XPATH,self.orders).click()

    @allure.step
    def products_click(self):
        self.driver.find_element(By.XPATH,self.products).click()

    @allure.step
    def sells_click(self):
        self.driver.find_element(By.XPATH,self.sells).click()

    @allure.step
    def stores_click(self):
        self.driver.find_element(By.XPATH,self.stores).click()

    @allure.step
    def users_click(self):
        self.driver.find_element(By.XPATH,self.users).click()

    # @allure.step
    # def all_navbar(self):
    #     util = Utilitis(self.driver)
    #     for i in range(1,7):
    #         data = "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/a[{}]/span[1]"
    #         if i == 2:
    #             continue
    #         self.driver.find_element(By.XPATH,self.allnav.format(i)).click()
    #         sleep(3)
    #         x = util.get_text(DashboardLocators.text)
    #         self.driver.implicitly_wait(5)
    #         u = self.driver.find_element(By.XPATH,data.format(i)).text
    #         print(u)
    #         if x != u:
    #             return False
    #         else:
    #             self.driver.back()
    #     return True







