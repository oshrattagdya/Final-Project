""" Locators for Categories screen"""

class CategoriesLocators:

    categories_nav_btn = "//nav[1]/div[2]/a[21]"
    search_categ_btn = "(//input[@type='search'])[1]"
    options = "(//i[@class='fa fa-ellipsis-v icon_icon '])"
    add_btn = "(//span[contains(text(),'הוספה')])[1]"
    name_field = "//input[@tabletype='string']"
    department_filed = "//input[contains(@placeholder,'מחלקות')]"
    fields_name = "(//input[@placeholder='שם'])[2]"
    type_field = "//input[@placeholder='סוג']"
    type_ops = "//div[contains(text(),'{}')]"
    add_submit = "//input[@value='הוספה']"
    product_status_op = "//span[@class='checkbox_checkboxCircle']"



