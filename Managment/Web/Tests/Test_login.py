import pytest
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Login_page import LoginPageFunc


@pytest.mark.usefixtures('set_up')

class TestLogin(Base):

    def test_login_success(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('1950000000')
        driver.implicitly_wait(10)
        login.click_on_button()
        driver.implicitly_wait(10)
        login.enter_phone_code('1234')
        login.click_on_button_login()






