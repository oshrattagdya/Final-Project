""" utils functions"""
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..Locators.Login_locators import Login_Locators
from ..Locators.Utils_locators import Utils_Locators
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Login_page import LoginPageFunc
from selenium.webdriver.remote.webdriver import WebDriver

class Utilitis():

    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.pesent_res = Utils_Locators.present_res
        self.res_amount = Utils_Locators.res_amount
        self.search_field = Utils_Locators.search_field
        self.table_res = Utils_Locators.table_res
        self.options_btn = Utils_Locators.options_btn
        self.add_btn = Utils_Locators.add_btn


    def select_result_amount(self,amount):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,self.pesent_res))
        ).click()

        option =  WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.res_amount.format(amount)))
        )
        option.click()



    def get_text(self,locator):
        text = self.driver.find_element(By.XPATH, locator).get_attribute("innerText")
        return text


    def connect_home_page(self):

        login = LoginPageFunc(self.driver)
        login.enter_phone('1950000000')
        self.driver.implicitly_wait(10)
        login.click_on_button()
        self.driver.implicitly_wait(10)
        login.enter_phone_code('1234')
        login.click_on_button_login()

    def search_box(self,name):
        self.name = name

        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.search_field))
        )

        search.send_keys(self.name)
        search.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.table_res))
        ).click()

    def JS_Message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.phone_field).get_attribute('validationMessage')

    def add(self):
        self.driver.find_element(By.CSS_SELECTOR,Utils_Locators.options_btn).click()
        self.driver.find_element(By.XPATH,Utils_Locators.add_btn).click()


    def serche_input(self,value):
        self.driver.find_element(By.XPATH, Utils_Locators.search_field).clear()
        self.driver.find_element(By.XPATH,Utils_Locators.search_field).send_keys(value)
        self.driver.find_element(By.XPATH,Utils_Locators.search_field).send_keys(Keys.ENTER)