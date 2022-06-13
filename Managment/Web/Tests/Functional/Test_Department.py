import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Department_page import DepartmentPageFunc
from selenium.webdriver.support import expected_conditions as EC
from Managment.Web.Utils.utils import Utilitis
import pyautogui


@pytest.mark.usefixtures('set_up')
class TestDepartment(Base):

    """test 1"""
    def test_Adding_a_department_success(self,):
        driver = self.driver
        util = Utilitis(driver)
        util.connect_home_page()
        add = DepartmentPageFunc(driver)
        add.click_department_button()
        time.sleep(2)
        util.addBtn()
        add.enter_name()
        add.add_photo()
        add.add_background_photo()
        add.click_on_add_button()
        time.sleep(5)
        util.search_box('סבונים')
        util.assertFunc(add.assertDepartment(),'סבונים')
        time.sleep(2)






