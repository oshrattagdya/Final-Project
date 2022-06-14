import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Department_page import DepartmentPageFunc
from selenium.webdriver.support import expected_conditions as EC
from Managment.Web.Utils.utils import Utilitis
import pyautogui

"""Test for department export"""
@pytest.mark.usefixtures('connect_home_page')
class TestDepartment(Base):

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
        util.addBtn()
        # Using the "enter name" function
        add.enter_name('תוספות')
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo()
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(2)
        # Using the "searchField" function
        util.searchField('תוספות')
        time.sleep(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), 'תוספות')

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
        # Using the login function
        util.connect_home_page()
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        #sleep
        time.sleep(3)
        # Using the "searchField" function
        util.searchField('461t')
        # Using the "assert" function
        util.assertFunc(add.searchDepartmentIncorrectly(), 'סה״כ: 0 שורות')

        """Tests for departments UI"""
    def test_ui_for_department_screen(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Using the login function
        util.connect_home_page()
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        #sleep
        time.sleep(3)
        # Using the "assert" function
        util.assertFunc(add.ui_txt_for_page(), "הוספה\nייצוא\nמזהה\n\tשם\n\tתמונה\n\tתמונת רקע\n\tפעיל\n\tתאריך יצירה\n\nu6z3r13kkkv9cqk3\tוודקה\t\n\t\n\t✓\t\n07/02/21, 16:44\n\n461hdlknbycfhy\tחלב\t\n\t\n\t✗\t\n10/04/21, 19:28\n\nu6z3r6pokm0lra0r\tקוניאק\t\n\t\n\t✓\t\n08/03/21, 15:10\n\nu6z3rgrckkzoqwou\tשוקולדים\t\n\t\n\t✓\t\n10/02/21, 19:06\n\npslidk0kp9nk6b0\tירוקו\t\n\t\n\t✓\t\n29/05/21, 14:10\n\nt4yw88klqifbu8\tבדיקה\t\n\t\n\t✓\t\n01/03/21, 13:39\n\n1k9pzmkz4i3awb\tקנאביס\t\n\t\n\t✓\t\n01/02/22, 21:15\n\nxfdpjewkz59964t\tבטון\t\n\t\n\t✓\t\n02/02/22, 09:55\n\n4jp555dl46ps70v\tfdgfd\t\n\t\n\t✓\t\n09/06/22, 10:44\n\n4jp555dl4birmvj\tyossi\t\n\t\n\t✓\t\n12/06/22, 19:27\n\n4jp555dl4cjmtpl\tסיגריות\t\n\t\n\t✓\t\nאתמול, 12:39\n\n4jp555dl4cjpcbx\tטבק\t\n\t\n\t✓\t\nאתמול, 12:41\n\n4jp555dl4cjqrn6\tטבק1\t\n\t\n\t✓\t\nאתמול, 12:42\n\n4jp555dl4cjxrvq\tסבונים\t\n\t\n\t✓\t\nאתמול, 12:47\n\n4jp555dl4ckigqp\tסבונים2\t\n\t\n\t✓\t\nאתמול, 13:03\n\n4jp555dl4curhv3\tסבוני12\t\n\t\n\t✓\t\nאתמול, 17:50\n\n4jp555dl4cvfr4h\tסבונים1\t\n\t\n\t✓\t\nאתמול, 18:09\n\n4jp555dl4cvhva3\tסבונים11\t\n\t\n\t✓\t\nאתמול, 18:11\n\n4jp555dl4cvmywv\tסבונים0\t\n\t\n\t✓\t\nאתמול, 18:15\n\n4jp555dl4cvpe6x\tסבונים09\t\n\t\n\t✓\t\nאתמול, 18:17\n\n4jp555dl4cw08c5\tסבונים111\t\n\t\n\t✓\t\nאתמול, 18:25\n\n4jp555dl4d0ebo9\tסבוניםם\t\n\t\n\t✓\t\nאתמול, 20:28\n\n4jp555dl4d5k2mx\tסבון\t\n\t\n\t✓\t\nאתמול, 22:52\n\n4jp555dl4d9p4v1\tנייר\t\n\t\n\t✓\t\nהיום, 00:48\n\n4jp555dl4d9qxox\tניירות\t\n\t\n\t✓\t\nהיום, 00:50\nמציג \n לעמוד\nסה״כ: 25 שורות")

    def test_ui_for_department_screen_menuBar(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Using the login function
        util.connect_home_page()
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        #sleep
        time.sleep(3)
        # Using the "assert" function
        util.assertFunc(add.ui_txt_for_menu_bar(),"מחלקות")

        """Tests for Department updates"""
    def test_Update_all_fields_properly_in_active_mode(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Using the login function
        util.connect_home_page()
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
        add.enter_name("מוצרי טיפוח")
        # Using the "add photo" function
        add.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo(r'''C:\Users\R.png''')
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False),'מוצרי טיפוח')

    def test_Update_all_fields_properly_in_inactive_mode(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Using the login function
        util.connect_home_page()
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        time.sleep(4)
        # Using the "enter name" function
        add.enter_name("מוצרי טיפוח")
        # Using the "add photo" function
        add.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo(r'''C:\Users\R.png''')
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False), 'מוצרי טיפוח')

    def  test_Update_properly_when_an_update_is_made_only_in_the_Name_field(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Using the login function
        util.connect_home_page()
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        time.sleep(4)
        # Using the "add photo" function
        add.add_photo()
        # Using the "add background photo" function
        add.add_background_photo()
        # Using the "click on update button" function
        add.click_on_update_button()
        time.sleep(5)
        # Using the "assert" function
        util.assertFunc(add.assert_img_src(), r'''"C:\Users\logo-linkedin-4096.png"''')

    def test_Update_properly_when_no_update_is_made(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Using the login function
        util.connect_home_page()
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        time.sleep(4)
        # Using the "click on update button" function
        add.click_on_update_button()
        time.sleep(5)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False), 'מוצרי טיפוח')

    def test(self):
        driver = self.driver
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        util = Utilitis(driver)
        util.secachItemValidation()






















