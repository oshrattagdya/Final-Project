import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Dashboard_page import DashboardPageFunc
from Managment.Web.Locators.Dashboard_locators import DashboardLocators
from Managment.Web.Utils.utils import Utilitis
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@pytest.mark.usefixtures('set_up')
class TestDashboard(Base):

    def test_navbar_btn(self):
        driver = self.driver
        dash = DashboardPageFunc(driver)
        util = Utilitis(driver)
        dash.connect()
        x = dash.all_navbar()
        assert x == True

        # dash.click_cup()
        # text_cupon = util.get_text(DashboardLocators.text)
        # assert text_cupon == "קופונים"
        # driver.back()
        # dash.orders_click()
        # order = util.get_text(DashboardLocators.text)
        # assert order == "הזמנות"
        # driver.back()
        # dash.products_click()
        # prod = util.get_text(DashboardLocators.text)
        # assert prod == "מוצרים"
        # driver.back()
        # dash.sells_click()
        # sel = util.get_text(DashboardLocators.text)
        # assert sel == "מבצעים"





