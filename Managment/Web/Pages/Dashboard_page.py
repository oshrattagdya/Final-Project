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

    def connect(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='טלפון']").send_keys('1950000000')
        self.driver.find_element(By.XPATH, "//input[@value='שלח לי קוד']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='קוד']").send_keys('1234')
        self.driver.find_element(By.XPATH, "//input[@value='כניסה']").click()

    def click_cup(self):
        self.driver.find_element(By.XPATH,self.cupons_button).click()


    def finnens_click(self):
        self.driver.find_element(By.XPATH,self.finnens).click()

    def orders_click(self):
        self.driver.find_element(By.XPATH,self.orders).click()

    def products_click(self):
        self.driver.find_element(By.XPATH,self.products).click()

    def sells_click(self):
        self.driver.find_element(By.XPATH,self.sells).click()

    def stores_click(self):
        self.driver.find_element(By.XPATH,self.stores).click()

    def users_click(self):
        self.driver.find_element(By.XPATH,self.users).click()

    def all_navbar(self):
        util = Utilitis(self.driver)
        data = ["קופונים","הזמנות","מוצרים","מבצעים","חנויות","משתמשים"]
        for i in range(1,7):
            for j in data:
                if i == 2:
                    continue
                self.driver.find_element(By.XPATH,self.allnav.format(i)).click()
                sleep(2)
                x = util.get_text(DashboardLocators.text)
                if x != j:
                    return False
                self.driver.back()
                return True






