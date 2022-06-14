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
        self.add_categ_button = CategoriesLocators.add_categ_button
        self.assert_name = CategoriesLocators.assert_name
        self.assert_dep = CategoriesLocators.assert_dep
        self.required_message_name = CategoriesLocators.required_message_name
        self.ab = "//label[contains(text(),'שדות')]"
        self.required_message_second_name_field = CategoriesLocators.required_message_second_name_field
        self.required_message_type_field = CategoriesLocators.required_message_type_field


    def click_categories_navbar(self):
        self.driver.find_element(By.XPATH,self.categories_nav_btn).click()
    # click on 3 dots button to open options
    def click_options_navbar(self):
        self.driver.find_element(By.XPATH,self.options).click()
    # click on add new category
    def click_add_btn(self):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,self.add_btn))
        ).click()
    # final step to add new category click on add button on form
    def click_submit_add_category(self):
        self.driver.find_element(By.XPATH,self.add_submit).click()
    # click on active option on form
    def click_status_active_op(self):
        self.driver.find_element(By.XPATH,self.product_status_op).click()


    #search for specific category on serach box
    def search_category(self,categ_name):
        self.categ_name = categ_name
        search = self.driver.find_element(By.XPATH,self.search_categ_btn)
        search.send_keys(self.categ_name)
        search.send_keys(Keys.RETURN)

    # insert new category name in add new category form
    def insert_new_category_name(self,new_categ_name):
        self.new_categ_name = new_categ_name
        self.driver.find_element(By.XPATH,self.name_field).send_keys(self.new_categ_name)

    # insert new department name in add new category form
    def insert_department_name(self,department_name):
        self.department_name = department_name
        self.driver.find_element(By.XPATH,self.department_filed).send_keys(self.department_name)
        self.driver.find_element(By.XPATH,"//div[@class='input_autocompleteItem ']").click()

    # insert new field name in add new category form
    def insert_field_name(self,field_name):
        self.field_name = field_name
        self.driver.find_element(By.XPATH,self.fields_name).send_keys(self.field_name)

    # select type option  in add new category form
    def type_option(self,op):
        self.driver.find_element(By.XPATH,self.type_field).click()

        options = self.driver.find_element(By.XPATH,self.type_ops.format(op))
        options.click()

    def click_on_category_add_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.add_categ_button).click()


    def get_text_name(self):
        return self.driver.find_element(By.XPATH,self.assert_name).get_attribute("innerText")


    def get_text_dep(self):
        return self.driver.find_element(By.XPATH,self.assert_dep).get_attribute("innerText")

    def get_required_message_name(self):
        return self.driver.find_element(By.XPATH,self.required_message_name).get_attribute("innerText")


    def click_none(self):
        self.driver.find_element(By.XPATH,self.ab).click()

    def get_required_message_second_name_field(self):
        return self.driver.find_element(By.XPATH,self.required_message_second_name_field).get_attribute("innerText")


    def get_required_message_type_field(self):
        return self.driver.find_element(By.XPATH,self.required_message_type_field).get_attribute("innerText")





