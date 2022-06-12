""" utils functions"""

from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base

class Utilitis():

    def __init__(self, driver):
        self.driver = driver

    def get_text(self,locator):
        text = self.driver.find_element(By.XPATH, locator).text
        return text




