import time
import pytest
from Managment.Web.Utils.utils import Utilitis
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Categories_page import CategoriesPageFunc
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('connect_home_page')
class TestCategories(Base):
    """test 1"""
    def test_add_new_category_to_my_store_correctly(self):
        driver = self.driver
        #using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        #entering the categories page
        category.click_categories_navbar()

        #clicking on adding a category
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        #insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)

        #insert department name
        category.insert_department_name("קוניאק")
        driver.implicitly_wait(10)

        #insert name field
        category.insert_field_name("גרב")
        driver.implicitly_wait(10)

        #select type
        category.type_option("טקסט")
        driver.implicitly_wait(10)

        #click on add
        category.click_on_category_add_button()
        time.sleep(3)
        driver.implicitly_wait(2)
        util.assertFunc(category.get_text_name(),"גרב")
        util.assertFunc(category.get_text_dep(),"קוניאק")

    """test 2"""
    def test_add_new_category_to_my_store_incorrectly_when_name_field_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        # util.connect_home_page()
        category = CategoriesPageFunc(driver)
        driver.implicitly_wait(10)

        # entering the categories page
        category.click_categories_navbar()
        time.sleep(3)
        driver.implicitly_wait(10)

        # clicking on adding a category
        util.addBtn()
        time.sleep(5)
        driver.implicitly_wait(10)

        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        # category.insert_new_category_name("גרבר")
        driver.implicitly_wait(10)

        #insert department name
        category.insert_department_name("קוניאק")
        driver.implicitly_wait(10)

        # insert name field
        category.insert_field_name("גרבר")
        driver.implicitly_wait(10)

        # select type
        category.type_option("טקסט")
        driver.implicitly_wait(10)

        # click on add
        category.click_on_category_add_button()
        time.sleep(3)
        driver.implicitly_wait(2)
        util.assertFunc(category.get_required_message_name(),"נא למלא שדה זה")

    """test 3"""
    def test_add_new_category_to_my_store_incorrectly_when_category_field_null(self):

        driver = self.driver
        #using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        #entering the categories page
        category.click_categories_navbar()

        #clicking on adding a category
        time.sleep(2)
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        #insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)

        #insert category name
        category.click_status_active_op()
        time.sleep(5)
        category.insert_new_category_name("גרב")

        # insert department name
        # category.insert_department_name("")

        #insert name field
        category.insert_field_name("גרב")

        #select type
        category.type_option("טקסט")

        #click on add
        category.click_on_category_add_button()
        category.click_none()
        driver.implicitly_wait(2)
        time.sleep(4)
        a = util.get_text("//div[contains(@class,'formItem_departmentIds')]//div[contains(@class,'form_note')][contains(text(),'נא למלא שדה זה')]")
        util.assertFunc(a,"נא למלא שדה זה")


    """test 4"""
    def test_add_new_category_to_my_store_incorrectly_when_second_name_field_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()

        # clicking on adding a category
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)

        # insert department name
        category.insert_department_name("קוניאק")
        # driver.implicitly_wait(10)

        # select type
        category.type_option("טקסט")
        time.sleep(5)
        # click on add
        category.click_on_category_add_button()
        time.sleep(7)
        driver.implicitly_wait(2)
        category.click_on_category_add_button()
        time.sleep(7)
        util.assertFunc(category.get_required_message_second_name_field() , "נא למלא שדה זה")

    """test 5"""
    def test_add_new_category_to_my_store_incorrectly_when_type_field_is_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()

        # clicking on adding a category
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)

        # insert department name
        category.insert_department_name("קוניאק")
        driver.implicitly_wait(10)

        # insert name field
        category.insert_field_name("גרב")
        driver.implicitly_wait(10)

        # # select type
        # category.type_option("טקסט")
        # driver.implicitly_wait(10)

        # click on add
        category.click_on_category_add_button()
        time.sleep(3)
        # category.click_on_category_add_button()
        # driver.find_element(By.XPATH,self.required_message_name).click()
        time.sleep(5)
        util.assertFunc(get_required_message_type_field(),"נא למלא שדה זה")

















