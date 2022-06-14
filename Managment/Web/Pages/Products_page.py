from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..Locators.Products_locators import ProductsLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
class ProductsPageFunc():
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.dasbord_products_btn = ProductsLocators.dasbord_products_btn
        self.product_status_op = ProductsLocators.product_status_op
        self.desc_boxs = ProductsLocators.desc_boxs
        self.barcode_field = ProductsLocators.barcode_field
        self.product_name_field = ProductsLocators.product_name_field
        self.product_price = ProductsLocators.product_price
        self.date_field = ProductsLocators.date_field
        self.next_btn = ProductsLocators.next_btn
        self.back_btn = ProductsLocators.back_btn
        self.cate_btn = ProductsLocators.cate_btn
        self.cate_op = ProductsLocators.cate_op
        self.store_btn = ProductsLocators.store_btn
        self.store_op = ProductsLocators.store_op
        self.dep_btn = ProductsLocators.dep_btn
        self.dep_auto_op = ProductsLocators.dep_auto_op
        self.kidom_field = ProductsLocators.kidom_field
        self.kidom_op = ProductsLocators.kidom_op
        self.yvoan_makbil = ProductsLocators.yvoan_makbil
        self.wight_btn = ProductsLocators.wight_btn
        self.wight_avg_per_unit_field = ProductsLocators.wight_avg_per_unit_field
        self.wight_unit_scale_btn = ProductsLocators.wight_unit_scale_btn
        self.scale_op = ProductsLocators.scale_op
        self.boxes_amout_field = ProductsLocators.boxes_amout_field
        self.amout_field = ProductsLocators.amout_field
        self.min_amout_field = ProductsLocators.min_amout_field
        self.city_field = ProductsLocators.city_field
        self.street_field = ProductsLocators.street_field
        self.home_num_field = ProductsLocators.home_num_field
        self.contact_num_field = ProductsLocators.contact_num_field


    def click_products_btn(self):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,self.dasbord_products_btn))
        ).click()




    def click_next_btn(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.next_btn))
        ).click()


    def click_back_btn(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.back_btn))
        ).click()



    def click_status_active_op(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.product_status_op))
        ).click()

    def set_mendetury_fields_of_product(self, barcode_data, product_name, product_price_data):
        self.barcode_data = barcode_data
        self.product_name = product_name
        self.product_price_data = product_price_data
        self.driver.find_element(By.XPATH, self.barcode_field).send_keys(self.barcode_data)

        self.driver.find_element(By.XPATH, self.product_name_field).send_keys(self.product_name)

        self.driver.find_element(By.XPATH, self.product_price).send_keys(self.product_price_data)







    def insert_expiration_date(self,expiration_date):
        self.expiration_date= expiration_date
        date = self.driver.find_element(By.XPATH, self.date_field)
        date.clear()
        date.send_keys(self.expiration_date)


    def category_option(self,op):
        self.driver.find_element(By.XPATH,self.cate_btn).click()

        options = self.driver.find_element(By.XPATH,self.cate_op.format(op))
        options.click()

    def dep_option(self,op):
        self.driver.find_element(By.XPATH,self.dep_btn).click()

        options = self.driver.find_elements(By.XPATH,self.store_op)
        options[op].click()

    def click_dep_auto_option(self):
        self.driver.find_element(By.XPATH,self.dep_auto_op).click()


    def click_yvoan_op(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.yvoan_makbil))
        ).click()



    def store_option(self,op):
        self.driver.find_element(By.XPATH,self.store_btn).click()

        options = self.driver.find_element(By.XPATH,self.store_op.format(op))
        options.click()

    def kidom_option(self,op):
        self.driver.find_element(By.XPATH,self.kidom_field).click()

        options = self.driver.find_elements(By.XPATH,self.kidom_op)
        options[op].click()


    def set_wight_op_on_with_data(self,op,wight):
        self.driver.find_element(By.XPATH,self.wight_btn).click()
        avg_wight = self.driver.find_element(By.XPATH,self.wight_avg_per_unit_field)
        avg_wight.send_keys(wight)
        self.driver.find_element(By.XPATH, self.wight_unit_scale_btn).click()
        options = self.driver.find_element(By.XPATH, self.scale_op.format(op))
        options.click()


    def set_boxes_amout_data(self,boxes,amount,min):
        boxes_amount = self.driver.find_element(By.XPATH, self.boxes_amout_field)
        boxes_amount.send_keys(boxes)

        total_amount = self.driver.find_element(By.XPATH, self.amout_field)
        total_amount.send_keys(amount)

        min_amount = self.driver.find_element(By.XPATH, self.min_amout_field)
        min_amount.send_keys(min)

    def set_address_data(self,city,street,home,contact):
        city_input = self.driver.find_element(By.XPATH, self.city_field)
        city_input.send_keys(city)

        street_input = self.driver.find_element(By.XPATH, self.street_field)
        street_input.send_keys(street)

        home_num_input = self.driver.find_element(By.XPATH, self.home_num_field)
        home_num_input.send_keys(home)

        contact_num_input = self.driver.find_element(By.XPATH, self.contact_num_field)
        contact_num_input.send_keys(contact)


    def description_details(self,desc):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.desc_boxs))
        ).send_keys(desc)












