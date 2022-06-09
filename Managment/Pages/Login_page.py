from Managment.Locators import Login_locators
from Managment.Locators.Login_locators import Login_Locators


class LoginPageFunc:
    def __init__(self, driver):
        self.driver = driver
        self.phone_field = Login_Locators.phone_field
