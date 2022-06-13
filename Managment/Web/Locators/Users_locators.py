""" Locators for Users screen"""

class UsersLocators:

    user_nav_btn = "//span[contains(text(),'משתמשים')]"


    #add users locators
    name = "//input[@placeholder='שם פרטי']"
    lastname = "//input[@placeholder='שם משפחה']"
    emil = "//input[@placeholder='דואר אלקטרוני']"
    phone = "//input[@placeholder='טלפון']"
    store = "//input[contains(@placeholder,'חנויות')]"
    store_ops = "//div[@class='input_autocompleteItem '][contains(text(),'{}')]"
    pick ="// body // div // span // div // div[2]"
    btnadd = "//input[@value='הוספה']"

    #assert locator
    varify = "//td[normalize-space()='{}']"