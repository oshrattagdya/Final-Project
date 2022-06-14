""" utils functions"""
from selenium.webdriver import Keys
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Managment.Web.Locators.Login_locators import Login_Locators
from ..Locators.Login_locators import Login_Locators
from ..Locators.Utils_locators import Utils_Locators
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from allure_commons.types import AttachmentType
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
        self.phone_field = Login_Locators.phone_field
        self.export_btn = Utils_Locators.export_btn
        self.photo_field = Utils_Locators.photo_field


    def select_result_amount(self,amount):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,self.pesent_res))
        ).click()

        option =  WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.res_amount.format(amount)))
        )
        option.click()



    def get_text(self,locator):
        text = self.driver.find_element(By.XPATH, locator).text
        return text



    def valid_Message(self,field):
        return self.driver.find_element(By.CSS_SELECTOR, self.field).get_attribute('validationMessage')

    def search_box(self,name):
        self.name = name

        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.search_field)))

        search.send_keys(self.name)
        search.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.table_res))).click()


    def addBtn(self):
        self.driver.find_element(By.CSS_SELECTOR,Utils_Locators.options_btn).click()
        self.driver.find_element(By.XPATH,Utils_Locators.add_btn).click()



    def assertFunc(self, a, b):

        driver = self.driver
        try:
            assert a == b
        except Exception as e:
            print('Error', format(e))
            raise allure.attach(self.driver.get_screenshot_as_png(), self.driver.save_screenshot("screenshot"),
                                attachment_type=AttachmentType.PNG)

    def exportBtn(self):
        self.driver.find_element(By.CSS_SELECTOR,Utils_Locators.options_btn).click()
        self.driver.find_element(By.XPATH,Utils_Locators.export_btn).click()

    def searchField(self,name):
        self.name = name
        search = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.search_field)))
        search.send_keys(self.name)
        search.send_keys(Keys.RETURN)

    def add_photo(self,url):
        self.driver.find_element(By.XPATH, self.photo_field).send_keys(f'''{url}''')


