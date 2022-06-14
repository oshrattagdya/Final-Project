import time

import pytest
import allure
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Products_page import ProductsPageFunc
from Managment.Web.Pages.Login_page import LoginPageFunc
from Managment.Web.Utils.utils import Utilitis


@pytest.mark.usefixtures('connect_home_page')
class TestProducts(Base):

    # 1
    def test_add_a_new_product_to_my_store_corrctly(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.addBtn()

        # upload photo
        pic = r'C:\Users\97253\Downloads\goats.jpg'
        util.add_photo(pic)
        # insert mendetury fields
        prod.set_mendetury_fields_of_product("011", "balls", 200)
        time.sleep(2)
        prod.click_next_btn()
        # stage 2
        prod.category_option("חטיפים")
        prod.click_dep_auto_option()
        prod.store_option("סופר כל רונן בע״מ")
        prod.kidom_option(0)
        time.sleep(2)
        prod.click_next_btn()
        # stage 3
        prod.set_wight_op_on_with_data("גרם", 100)
        prod.set_boxes_amout_data(100, 20, 10)
        time.sleep(2)
        prod.click_next_btn()
        # stage 4
        prod.set_address_data("tel-aviv", "brzil", 100, "0542259745")
        time.sleep(2)
        prod.click_next_btn()
        # stage 5
        prod.description_details(" with pic  upload")
        prod.click_status_active_op()
        time.sleep(2)
        prod.click_next_btn()
        time.sleep(15)
        driver.refresh()
        util.searchField("011")

        value = util.get_text("//table[1]/tbody[1]/tr[1]/td[3]")
        print(value)
        assert value == "balls"

    # 2
    def test_add_a_new_product_to_my_store_incorrctly_when_barcode_field_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.addBtn()

        prod.set_mendetury_fields_of_product("", "full", 100)
        prod.click_next_btn()

        message = util.valid_Message(prod.barcode_field)
        assert message == "Please fill out this field."

    # 2
    def test_add_a_new_product_to_my_store_incorrctly_when_name_field_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.addBtn()

        prod.set_mendetury_fields_of_product("03", "", 100)
        prod.click_next_btn()

        message = util.valid_Message(prod.product_name_field)
        assert message == "Please fill out this field."


    # 3
    def test_add_a_new_product_to_my_store_incorrctly_when_price_field_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.addBtn()

        prod.set_mendetury_fields_of_product("033", "qa", "")
        prod.click_next_btn()

        message = util.valid_Message(prod.product_price)
        assert message == "Please fill out this field."

    #4
    def test_add_a_new_product_to_my_store_incorrctly_when_all_field_are_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.addBtn()

        prod.set_mendetury_fields_of_product("", "", "")
        prod.click_next_btn()
        time.sleep(2)

        message = util.valid_Message(prod.barcode_field)
        assert message == "Please fill out this field."

    #test stage 2
    #5

    def test_add_a_new_product_to_my_store_incorrctly_when_category_field_are_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.addBtn()

        prod.set_mendetury_fields_of_product("44", "test", "100")
        prod.click_next_btn()


        prod.kidom_option(0)
        prod.store_option("סופר כל רונן בע״מ")
        prod.click_next_btn()


        message = util.valid_Message(prod.store_btn)

        assert message == "Please fill out this field."


        time.sleep(5)

    # 6
    def test_add_a_new_product_to_my_store_incorrctly_when_store_field_are_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.addBtn()

        prod.set_mendetury_fields_of_product("44", "test", "100")
        prod.click_next_btn()
        prod.category_option("חטיפים")
        prod.click_dep_auto_option()
        prod.kidom_option(0)
        prod.click_next_btn()

        message = util.valid_Message(prod.store_btn)

        assert message == "Please fill out this field."

        time.sleep(5)















