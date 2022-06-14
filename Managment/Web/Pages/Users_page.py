from Managment.Web.Locators.Users_locators import UsersLocators
from selenium.webdriver.common.by import By
from Managment.Web.Utils.utils import Utilitis
from time import sleep




class Userspagefunc():
    def __init__(self, driver):
        self.driver = driver
        self.user_nav_btn = UsersLocators.user_nav_btn
        self.name = UsersLocators.name
        self.lastname = UsersLocators.lastname
        self.emil = UsersLocators.emil
        self.phone = UsersLocators.phone
        self.store = UsersLocators.store
        self.store_ops = UsersLocators.store_ops
        self.pick = UsersLocators.pick
        self.btnadd = UsersLocators.btnadd
        self.varify = UsersLocators.varify




    def userpage_btn(self):
        self.driver.find_element(By.XPATH, self.user_nav_btn).click()

    def addname(self,name):
        self.driver.find_element(By.XPATH,self.name).click()
        self.driver.find_element(By.XPATH,self.name).send_keys(name)

    def addlastname(self,lastname):
        self.driver.find_element(By.XPATH,self.lastname).click()
        self.driver.find_element(By.XPATH,self.lastname).send_keys(lastname)

    def addemil(self,emil):
        self.driver.find_element(By.XPATH,self.emil).click()
        self.driver.find_element(By.XPATH,self.emil).send_keys(emil)

    def addphone(self,phone):
        self.driver.find_element(By.XPATH,self.phone).click()
        self.driver.find_element(By.XPATH,self.phone).send_keys(phone)

    def store_option(self, op):
        self.driver.find_element(By.XPATH, self.store).click()

        options = self.driver.find_element(By.XPATH, self.store_ops.format(op))
        options.click()


    def store_option_click(self, op):
        self.driver.find_element(By.XPATH, self.store).click()

    def add_btn(self):
        self.driver.find_element(By.XPATH,self.btnadd).click()


    def get_text(self,locator,x):
        text = self.driver.find_element(By.XPATH, locator.format(x)).text
        return text
