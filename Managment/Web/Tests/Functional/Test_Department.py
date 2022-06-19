import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Department_page import DepartmentPageFunc
from selenium.webdriver.support import expected_conditions as EC
from Managment.Web.Utils.utils import Utilitis
from Managment.DB.BaseMongoDB2 import MongoDB

DB = MongoDB("trado_qa", "department")


@pytest.mark.usefixtures('connect_home_page')
class TestDepartment(Base):

    """Test for department export"""
    def test_Export_departments_properly_success(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # Using the "export button" function
        util.exportBtn()
        time.sleep(3)



    """Tests for Creating a new department"""
    def test_Adding_a_department_success(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        driver.implicitly_wait(2)
        # Using the "add button" function
        time.sleep(3)
        util.addBtn(True)
        # Using the "random string" function
        name = util.randomString()
        # Using the "enter name" function
        add.enter_name(name)
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo()
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(2)
        # Using the "searchField" function
        util.searchField(name)
        time.sleep(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), name)
        print(DB.find([name]))
        # util.assertFunc(DB.find(["name"]))

    def test_Create_a_new_department_invalid_when_all_fields_are_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(3)
        # Using the "add button" function
        util.addBtn()
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(3)
        # Using the "assert" function
        util.assertFunc(add.assertDepartmentError(), 'נא למלא שדה זה')

    def test_Create_a_new_department_invalid_when_a_name_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn()
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo()
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartmentError(), 'נא למלא שדה זה')

    def test_Create_a_new_department_correctly_when_image_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn()
        # Using the "enter name" function
        add.enter_name('תכשיטים')
        # Using the "add background photo" function
        add.add_background_photo()
        # Using the "click on add button" function
        add.click_on_add_button()
        # Using the "searchField" function
        util.searchField('תכשיטים')
        driver.implicitly_wait(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), 'תכשיטים')

    def test_Create_a_new_department_correctly_when_a_Background_photo_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn()
        # Using the "enter name" function
        add.enter_name('נעלים')
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "click on add button" function
        add.click_on_add_button()
        # Using the "searchField" function
        util.searchField('נעלים')
        time.sleep(3)
        driver.implicitly_wait(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), 'נעלים')
        time.sleep(4)

    def test_Create_a_new_department_invalid_when_name_and_image_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn()
        # Using the "add background photo" function
        add.add_background_photo()
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartmentError(), 'נא למלא שדה זה')

    def test_Create_a_new_department_correctly_when_Background_photo_and_image_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn()
        # Using the "enter name" function
        add.enter_name('מסכות')
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(10)
        # Using the "searchField" function
        util.searchField('מסכות')
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), 'מסכות')
        time.sleep(5)

    def test_Create_a_new_department_invalid_when_Background_photo_and_name_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn()
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartmentError(), 'נא למלא שדה זה')

    """Tests for departments search"""
    def test_Valid_search_when_Identifier_correctly(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "searchField" function
        util.searchField('חלב')
        # Using the "assert" function
        util.assertFunc(add.searchIdentifier(), '461hdlknbycfhy')

    def test_Search_properly_when_products_are_available(self):
        driver = self.driver
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        util = Utilitis(driver)
        util.secachItemValidation()

    def test_Invalid_search_when_Identifier_incorrect(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "searchField" function
        util.searchField('461hdlkn2fhy')
        # Using the "assert" function
        util.assertFunc(add.searchDepartmentIncorrectly(), 'סה״כ: 0 שורות')

    def test_Invalid_search_when_name_incorrect(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        #sleep
        time.sleep(3)
        item = ['קפה', ' שיער', 'בובות', 'מבצעים', 'מעדנים', 'בריאות', 'קנאביס רפואי', 'ירוק', 'קיק', 'אבקה']
        for j in item:
            util.searchField(j)
            time.sleep(6)
            assert (add.searchDepartmentIncorrectly(), 'סה״כ: 0 שורות')
            print(f" {j} is correct")

        """Tests for departments update"""
    def test_Update_all_fields_properly_in_active_mode(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        time.sleep(4)
        # Using the "click_on_active_button" function
        add.click_on_active_button()
        # Using the "enter name" function
        add.enter_name("מברשות")
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo()
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False),'מברשות')

    def test_Update_all_fields_properly_in_inactive_mode(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        time.sleep(4)
        # Using the "enter name" function
        add.enter_name("חשמל1")
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo()
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False), 'חשמל1')

    def test_Update_properly_when_an_update_is_made_only_in_the_Name_field(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)

        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "enter name" function
        add.enter_name('נביעות')
        # Using the "click on update button" function
        add.click_on_update_button()
        time.sleep(5)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False), 'נביעות')

    def test_Update_properly_when_no_update_is_made(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False), 'נביעות')

    def test_Update_properly_when_an_update_is_made_only_in_the_Background_photo_field(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\logo-linkedin-4096.png''')
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        time.sleep(6)
        print(add.assert_img_src_photo())
        util.assertFunc(add.assert_img_src_photo(),'https://storage.cloud.google.com/trado_images/department/461hdlknbycfhypslie6ckppafmkm-1655315881737')

    def test_Update_properly_when_an_update_is_made_only_in_the__photo_field(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "add photo" function
        add.add_background_photo()
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        a = driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/div[1]/img[1]").get_attribute("src")
        time.sleep(6)
        util.assertFunc(add.img_src_position_2)
        # assert a == "https://storage.cloud.google.com/trado_images/department/461hdlknbycfhypslie6ckppafmkm-1655322100824"


    def test(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)

        res =util.randomString()
        print(res)


























