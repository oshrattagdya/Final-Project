import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Dashboard_page import DashboardPageFunc
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures('set_up')
class TestDashboard(Base):

    def test_btn(self):
        driver = self.driver
        dash = DashboardPageFunc(driver)
        dash.connect()
        driver.implicitly_wait(10)
        dash.cupons_button()


