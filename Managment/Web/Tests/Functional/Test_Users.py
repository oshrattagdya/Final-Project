import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Users_page import Userspagefunc
from Managment.Web.Locators.Dashboard_locators import DashboardLocators
from Managment.Web.Utils.utils import Utilitis
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@pytest.mark.usefixtures('set_up')
class TestUsers(Base):

    def test_valid_addUser(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        util.connect_home_page()
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn()
        user.addname("avi")
        user.addlastname("jambar")
        user.addemil("j@jd.com")
        user.addphone("195222224")
        user.store_option("dddd")
        user.add_btn()
        val = user.get_text(user.varify,"avi")
        util.assertFunc(val,"avi")
        sleep(2)


    def test_invalid_emailNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        util.connect_home_page()
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn()
        user.addname("sd")
        user.addlastname("jambar")
        user.addemil("")
        user.addphone("195222223")
        user.store_option("dddd")
        user.add_btn()
        val = util.get_text("//div[contains(text(),'דוא״ל לא תקין')]")
        util.assertFunc(val ,'דוא״ל לא תקין')
        sleep(2)

    def test_phoneNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        util.connect_home_page()
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn()
        user.addname("sd")
        user.addlastname("jambar")
        user.addemil("d@j.com")
        user.addphone("")
        user.store_option("dddd")
        user.add_btn()
        val = util.get_text("//div[contains(text(),'מס׳ טלפון לא תקין')]")
        util.assertFunc(val ,'מס׳ טלפון לא תקין')


    def test_storeNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        util.connect_home_page()
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn()
        user.addname("sd")
        user.addlastname("jambar")
        user.addemil("d@j.com")
        user.addphone("195222225")
        user.store_option_click('')
        user.add_btn()
        val = util.get_text("//div[contains(text(),'נא למלא שדה זה')]")
        util.assertFunc(val ,'נא למלא שדה זה')
