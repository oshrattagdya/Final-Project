import time

import pytest
import allure
from selenium.webdriver.common.by import By
import os.path
from Managment.DB.BaseMongoDB2 import MongoDB
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Products_page import ProductsPageFunc
from Managment.Web.Pages.Login_page import LoginPageFunc
from Managment.Web.Utils.utils import Utilitis
db = MongoDB("trado_qa", "products")

@pytest.mark.usefixtures('connect_home_page')
class TestProducts(Base):



    # 1
    def test_add_a_new_product_to_my_store_corrctly(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn()

        # upload photo
        # pic = r'C:\Users\97253\Downloads\goats.jpg'
        # util.add_photo(pic)
        # insert mendetury fields
        prod.set_mendetury_fields_of_product("017", "hair cream", 35)
        time.sleep(2)
        prod.click_next_btn()
        # stage 2
        prod.category_option("פרחים")
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
        prod.set_address_data("tel-aviv", "tekva", 100, "0542259745")
        time.sleep(2)
        prod.click_next_btn()
        # stage 5
        prod.description_details("prigat   upload")
        prod.click_status_active_op()
        time.sleep(2)
        prod.click_next_btn()
        time.sleep(5)
        driver.refresh()
        util.searchField("017")

        value = util.get_text("//table[1]/tbody[1]/tr[1]/td[3]")
        print(value)
        assert value == "hair cream"

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
        time.sleep(1)
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
        # price field null
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
        # all fields null
        prod.set_mendetury_fields_of_product("", "", "")
        prod.click_next_btn()

        message = util.valid_Message(prod.barcode_field)
        assert message == "Please fill out this field."

    #5  test stage 2

    def test_add_a_new_product_to_my_store_incorrctly_when_category_field_are_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        util.addBtn()
        #stage 1
        prod.set_mendetury_fields_of_product("44", "test", "100")
        prod.click_next_btn()
        # stage 2 fill all fields apart from category option
        prod.kidom_option(0)
        prod.store_option("סופר כל רונן בע״מ")
        prod.click_next_btn()
        message = util.valid_Message(prod.store_btn)

        assert message == "Please fill out this field."


    # 6
    def test_add_a_new_product_to_my_store_incorrctly_when_store_field_are_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        time.sleep(2)
        util.addBtn()
        #stage 1
        prod.set_mendetury_fields_of_product("44", "test", "100")
        prod.click_next_btn()
        #stage 2 fill all fields apart from store option
        prod.category_option("חטיפים")
        prod.click_dep_auto_option()
        prod.kidom_option(0)
        prod.click_next_btn()

        message = util.valid_Message(prod.store_btn)


        assert message == "Please fill out this field."


    #7
    def test_search_for_specific_product_and_edit_a_product_info_to_my_store_corrctly(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        #search for a product to edit
        util.search_box("voadka")
        #change date
        prod.insert_barcode_name("7899")
        prod.insert_product_name("voadka2k")
        prod.insert_product_price("85")
        for i in range(5):
            prod.click_next_btn()
        driver.refresh()

        util.searchField("7899")
        value = prod.row_details("name")
        util.assertFunc(value,"voadka2k")

    # 8
    def test_edit_a_product_info_incorrctly_when_price_is_letters(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("testagin")
        # change date
        prod.insert_product_price("handred")
        message = util.valid_Message(prod.product_price)
        expected_result = "Please enter a number."
        prod.click_next_btn()
        util.assertFunc(message,expected_result)
    #9
    def test_edit_a_product_info_incorrctly_when_barcode_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("testagin")
        # change date
        prod.insert_barcode_name("")
        message = util.valid_Message(prod.barcode_field)

        expected_result = "Please fill out this field."
        prod.click_next_btn()
        util.assertFunc(message,expected_result)
    #10
    def test_edit_a_product_info_incorrctly_when_name_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("testagin")
        # change date
        prod.insert_product_name("")
        message = util.valid_Message(prod.product_name_field)

        expected_result = "Please fill out this field."
        prod.click_next_btn()
        util.assertFunc(message, expected_result)


    #11
    def test_to_edit_a_product_incorractly_when_catagory_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("017")

        prod.click_next_btn()
        prod.clear_category_field()

        prod.click_next_btn()
        message = util.valid_Message(prod.cate_btn)
        expected_result = "Please fill out this field."
        util.assertFunc(message,expected_result)

    # 12
    def test_to_edit_a_product_incorractly_when_store_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("xfv")

        prod.click_next_btn()
        prod.clear_store_field()
        #make click no yvoan op to close store pop window
        prod.click_yvoan_op()

        prod.click_next_btn()
        message = util.valid_Message(prod.store_btn)
        expected_result = "Please fill out this field."
        util.assertFunc(message, expected_result)


    # 13

    def test_activate_product_status_succsessfully(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("017")
        time.sleep(2)
        #activate product status on
        prod.click_status_active_op()
        time.sleep(2)
        for i in range(5):
            prod.click_next_btn()
        time.sleep(2)
        driver.refresh()

        util.searchField("017")

        util.assertFunc(prod.row_details("status"),"✓")


    # 14
    def test_deactivate_product_status_succsessfully(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("017")
        time.sleep(2)
        # activate product status on
        prod.click_status_active_op()
        time.sleep(2)
        prod.click_next_number_off_times(5)

        util.searchField("017")

        util.assertFunc(prod.row_details("status"), '✗')


    #15

    def test_edit_product_description_succsessfully(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.searchField("666")
        prod.click_write_desc_to_product()
        descprtion_to_write = "\nadd new comment"
        prod.write_desc_to_product(descprtion_to_write)
        prod.cilck_save_desc_chages()
        time.sleep(2)
        prod.click_write_desc_to_product()
        descprtion = util.get_text(prod.writing_box)
        print(descprtion)
        data = db.find({"barcode": "666"})
        expected_result = data['description'][3:-5]
        print(expected_result)
        # validation with data base
        util.assertFunc(descprtion_to_write,expected_result)


    #16
    def test_export_file_to_pc(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        time.sleep(2)
        util.exportBtn()

        driver.implicitly_wait(30)
        time.sleep(10)
        while not os.path.exists(r"C:\Users\97253\Downloads\מוצרים - 15.06.22.csv"):
            time.sleep(1)

            if os.path.isfile(r"C:\Users\97253\Downloads\מוצרים - 15.06.22.csv"):
                print("file exesist")

    data = MongoDB("trado_qa", "products").find({"barcode": "sss"})
    expected_result = data['description'][3:-5]
    print(expected_result)





























