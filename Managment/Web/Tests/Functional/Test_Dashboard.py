import time

import allure
import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Dashboard_page import DashboardPageFunc
from Managment.Web.Locators.Dashboard_locators import DashboardLocators
from Managment.Web.Utils.utils import Utilitis
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@pytest.mark.usefixtures('connect_home_page')
class TestDashboard(Base):


    def test(self):
        driver = self.driver
        dash = DashboardPageFunc(driver)
        txt = ['קופונים', 'Finances', 'הזמנות', 'מוצרים', 'מבצעים', 'חנויות', 'משתמשים', 'Finances']
        util = Utilitis(driver)
        for i in range(1,8):
            if i == 2 :
                continue
            driver.find_element(By.XPATH,f"(//a[contains(@class,'dashboard_count')])[{i}]").click()
            time.sleep(2)
            header = util.get_text(DashboardLocators.text)
            # assert header == txt[i-1]
            util.assertFunc(header,txt[i-1])
            driver.back()
            time.sleep(2)


            # a.click()
            # assert util.get_text(DashboardLocators.text) == 'קופונים'


    def test_navbar_btn(self):
        driver = self.driver
        dash = DashboardPageFunc(driver)
        util = Utilitis(driver)
        dash.click_cup()
        text_cupon = util.get_text(DashboardLocators.text)
        util.assertFunc(text_cupon,"קופונים")
        driver.back()
        dash.orders_click()
        order = util.get_text(DashboardLocators.text)
        util.assertFunc(order, "הזמנות")
        driver.back()
        dash.products_click()
        prod = util.get_text(DashboardLocators.text)
        util.assertFunc(prod, "מוצרים")
        driver.back()
        dash.sells_click()
        sel = util.get_text(DashboardLocators.text)
        util.assertFunc(sel, "מבצעים")
        driver.back()
        dash.stores_click()
        store = util.get_text(DashboardLocators.text)
        util.assertFunc(store, "חנויות")
        driver.back()
        dash.users_click()
        user = util.get_text(DashboardLocators.text)
        util.assertFunc(user, "משתמשים")





