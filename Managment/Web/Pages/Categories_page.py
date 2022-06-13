from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..Locators.Categories_locators import CategoriesLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CategoriesPageFunc():
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.categories_nav_btn = CategoriesLocators.categories_nav_btn
        self.search_categ_btn = CategoriesLocators.search_categ_btn
        self.options = CategoriesLocators.options
        self.add_btn = CategoriesLocators.add_btn
        self.name_field = CategoriesLocators.name_field
        self.department_filed = CategoriesLocators.department_filed
        self.fields_name = CategoriesLocators.fields_name
        self.type_field = CategoriesLocators.type_field
        self.type_ops = CategoriesLocators.type_ops
        self.add_submit = CategoriesLocators.add_submit
        self.product_status_op = CategoriesLocators.product_status_op

    def click_categories_navbar(self):
        self.driver.find_element(By.XPATH,self.categories_nav_btn).click()

    def click_options_navbar(self):
        self.driver.find_element(By.XPATH,self.options).click()

    def click_add_btn(self):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,self.add_btn))
        ).click()

    def click_submit_add_category(self):
        self.driver.find_element(By.XPATH,self.add_submit).click()

    def click_status_active_op(self):
        self.driver.find_element(By.XPATH,self.product_status_op).click()



    def search_category(self,categ_name):
        self.categ_name = categ_name
        search = self.driver.find_element(By.XPATH,self.search_categ_btn)
        search.send_keys(self.categ_name)
        search.send_keys(Keys.RETURN)

    def insert_new_category_name(self,new_categ_name):
        self.new_categ_name = new_categ_name
        self.driver.find_element(By.XPATH,self.name_field).send_keys(self.new_categ_name)


    def insert_department_name(self,department_name):
        self.department_name = department_name
        self.driver.find_element(By.XPATH,self.department_filed).send_keys(self.department_name)


    def insert_field_name(self,field_name):
        self.field_name = field_name
        self.driver.find_element(By.XPATH,self.fields_name).send_keys(self.field_name)

    def type_option(self,op):
        self.driver.find_element(By.XPATH,self.type_field).click()

        options = self.driver.find_element(By.XPATH,self.type_ops.format(op))
        options.click()






