import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Users_page import Userspagefunc
from Managment.Web.Locators.Users_locators import UsersLocators
from Managment.Web.Utils.utils import Utilitis
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Managment.DB.BaseMongoDB2 import MongoDB
# db = MongoDB("trado_qa", "products")





@pytest.mark.usefixtures('connect_home_page')
class TestUsers(Base):

    #1
    def test_valid_addUser(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        db = MongoDB("trado_qa", "users")
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        user.addname("avi")
        user.addlastname("jambar")
        user.addemil("j@jdj.com")
        user.addphone("195222228")
        user.store_option("dddd")
        user.add_btn()
        val = user.get_text(user.varify,"avi")
        sleep(2)
        data = db.find({'email':"j@jdj.com"})
        util.assertFunc(val,data['firstName'])




    #2
    def test_invalid_emailNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn()
        user.addname("sd")
        user.addlastname("jambar")
        user.addemil("")
        user.addphone("1952222233")
        user.store_option("dddd")
        user.add_btn()
        emil = util.get_text(UsersLocators.eror_note)
        util.assertFunc(emil ,'דוא״ל לא תקין')
        sleep(2)


    #3
    def test_phoneNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
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
        val = util.get_text(UsersLocators.eror_note)
        util.assertFunc(val ,'מס׳ טלפון לא תקין')


    #4
    def test_storeNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn()
        user.addname("sd")
        user.addlastname("jambar")
        user.addemil("d@j.com")
        user.addphone("1952222227")
        sleep(3)
        user.store_option_click()
        user.add_btn()
        store = util.get_text(UsersLocators.eror_note)
        util.assertFunc(store,'נא למלא שדה זה')


    #5
    def test_serch_User_name(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        util.search_box("ישראל")
        name = util.get_text("//tbody/tr[1]/td[1]")
        util.assertFunc(name,"ישראל")


    #6
    def test_serch_User_lastname(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        util.search_box("מנגיסטו")
        emil = util.get_text("//tbody/tr[1]/td[2]")
        util.assertFunc(emil,"מנגיסטו")


    #7
    def test_serch_User_phone(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        util.search_box("0549703147")
        phone = util.get_text("//tbody/tr[1]/td[4]")
        util.assertFunc(phone,"0549703147")

    #8
    def test_valid_update(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        user.update_click()
        user.addname("as")
        user.addlastname("jambi")
        user.addemil("ddd@dJ.com")
        user.addphone("1952222239")
        user.store_option("shula")
        user.update_btn()
        sleep(2)
        name = util.get_text(UsersLocators.update)
        util.assertFunc(name,"as")


    #9
    def test_update_when_store_null(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        user.update_click()
        sleep(2)
        user.addname("as")
        user.addlastname("jambi")
        user.addemil("ddd@ddJ.com")
        user.addphone("1952222229")
        user.store_option("")
        user.update_btn()
        sleep(2)
        a = user.get_text(UsersLocators.update)
        util.assertFunc(a,"as")



