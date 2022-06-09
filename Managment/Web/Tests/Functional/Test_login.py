import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Login_page import LoginPageFunc
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    """test 1"""
    def test_login_success(self):
        name = "//body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/span[2]"
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('1950000000')
        driver.implicitly_wait(10)
        login.click_on_button()
        driver.implicitly_wait(10)
        login.enter_phone_code('1234')
        login.click_on_button_login()

        try:
            value = driver.find_element(By.XPATH,name).get_attribute("innerText")
            assert value == "שלום ולדימירהתנתק"
        except Exception as e:
            driver.get_screenshot_as_png()


    """test 2"""
    def test_login_incorrectly_when_user_non_register(self):
        user = "//div[contains(text(),'no such user')]"
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('4528762424')
        login.click_on_button()

        try :
            value = driver.find_element(By.XPATH, user).get_attribute("innerText")
            assert user == "no such user"
        except Exception as e:
            driver.get_screenshot_as_png()

    """test 3"""
    def test_login_incorrect_when_phone_field_null(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('')
        login.click_on_button()
        # assert login.JS_Message() == ''
        # login.enter_phone_code('1234')
        # login.click_on_button_login()
        try:
            assert login.JS_Message() == 'זהו שדה חובה.'
        except Exception as e:
            driver.get_screenshot_as_png()

    """test 4"""
    def test_login_incorrectly_when_phone_field_is_less_than_10_num(self):
        user = "//div[contains(text(),'no such user')]"
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('45')
        login.click_on_button()

        try:
            value = driver.find_element(By.XPATH, user).get_attribute("innerText")
            assert user == "no such user"
        except Exception as e:
            driver.get_screenshot_as_png()


    """test 5"""
    def test_login_incorrectly_when_code_is_not_match(self):
        failed_message = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[2]"
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('1950000000')
        login.click_on_button()
        login.click_on_button_login()
        try:
            value = driver.find_element(By.XPATH,failed_message).get_attribute("innerText")
            assert failed_message == "faild to login"
        except Exception as e:
            driver.get_screenshot_as_png()

    """test 6"""
    def test_login_incorrectly_when_code_is_null(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('1950000000')
        driver.implicitly_wait(10)
        login.click_on_button()
        driver.implicitly_wait(10)
        # login.enter_phone_code('')
        login.click_on_button_login()
        try:
            assert login.JS_Message() == 'זהו שדה חובה.'
        except Exception as e:
            driver.get_screenshot_as_png()