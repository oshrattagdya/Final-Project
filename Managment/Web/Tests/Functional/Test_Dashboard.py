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


    def test_navbar_btn(self):
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
            util.assertFunc(header,txt[i-1])
            driver.back()
            time.sleep(2)





    def test_ui(self):
        driver = self.driver
        dash = DashboardPageFunc(driver)
        util = Utilitis(driver)
        dash.graf_display()
        sum = dash.avrage()
        util.assertFunc(sum,'₪8753.01')
        ord = dash.order_()
        util.assertFunc(ord,"7")



