import pytest
import random
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Users_page import Userspagefunc
from Managment.Web.Locators.Users_locators import UsersLocators
from Managment.Web.Utils.utils import Utilitis
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Managment.DB.BaseMongoDB2 import MongoDB
db = MongoDB("trado_qa", "users")





@pytest.mark.usefixtures('connect_home_page')
class TestUsers(Base):

    #1
    def test_valid_addUser(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        user.addname(util.randomString())
        user.addlastname("jambar")
        user.addemil("j@jdj.com")
        phone = util.random_with_N_digits(10)
        user.addphone(phone)
        user.store_option("dddd")
        user.add_btn()
        val = user.get_text1(user.varify,phone)
        sleep(2)
        data = db.find({'phone':phone})
        util.assertFunc(val,data['phone'])

    def test_valid_addUser1(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        user.addname("")
        user.addlastname("")
        user.addemil("")
        user.addphone(util.random_with_N_digits(10))
        user.store_option("")
        user.add_btn()
        val = util.get_text(user.varify)
        sleep(2)


    #2
    def test_invalid_emailNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        user.addname("sd")
        user.addlastname("jambar")
        user.addemil("")
        user.addphone(util.random_with_N_digits(10))
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
        util.addBtn(True)
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
        util.addBtn(True)
        user.addname("sd")
        user.addlastname("jambar")
        user.addemil("d@j.com")
        user.addphone(util.random_with_N_digits(10))
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
        name = util.get_text("tbody:nth-child(2) tr:nth-child(1) > td:nth-child(1)")
        util.assertFunc(name,"ישראל")
        data = db.find('firstName')
        util.assertFunc(name, data['firstName'])

    #6
    def test_serch_User_lastname(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        util.search_box("מנגיסטו")
        lastname = util.get_text("tbody:nth-child(2) tr:nth-child(1) > td:nth-child(2)")
        util.assertFunc(lastname,"מנגיסטו")


    #7
    def test_serch_User_phone(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        util.search_box("0549703147")
        phone = util.get_text("tbody tr:nth-child(1) td:nth-child(4)")
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
        user.addphone(util.random_with_N_digits(10))
        user.store_option("shula")
        user.update_btn()
        sleep(2)
        name = util.get_text("tbody:nth-child(2) tr:nth-child(1) > td:nth-child(1)")
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
        user.addphone(util.random_with_N_digits(10))
        # user.store_option("")
        driver.find_element(By.CSS_SELECTOR,"div[class='tag_tag'] span").click()
        user.update_btn()
        driver.find_element(By.XPATH,"//label[contains(text(),'כתובת')]").click()
        eror = util.get_text("div[class='form_note ']")
        util.assertFunc(eror,"נא למלא שדה זה")



