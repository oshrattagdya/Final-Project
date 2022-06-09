from Managment.Web.Locators.Login_locators import Login_Locators
from selenium.webdriver.common.by import By


class LoginPageFunc:
    def __init__(self, driver):
        self.driver = driver
        self.phone_field = Login_Locators.phone_field
        self.code_field = Login_Locators.code_field
        self.button = Login_Locators.button



    def enter_phone(self,phone):
        self.driver.find_element(By.,self.phone_field).clear()
        self.driver.find_element(By.CLASS_NAME,self.phone_field).send_keys(phone)

    def enter_phone_code(self,phone_code):
        self.driver.find_element(By.CLASS_NAME,self.code_field).clear()
        self.driver.find_element(By.CLASS_NAME,self.code_field).send_keys(phone_code)

    def click_on_button(self):
        self.driver.find_element(By.CLASS_NAME,self.button).click()








