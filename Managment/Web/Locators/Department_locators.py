""" Locators for department screen"""

class Department_Locators:

    """ Locators for Adding departments"""
    departmet_button = "a:nth-child(24) span:nth-child(2)"
    name_field = "input[placeholder='שם']"
    phone_field = "(//input[contains(@type,'file')])[1]"
    background_photo = "(//input[contains(@type,'file')])[2]"
    add_button = "input[value='הוספה']"
    activ_button = ".checkbox_checkboxCircle"
    assert_txt = "//tbody/tr/td[2]"
    assert_txt_error = "//div[@class='form_note ']"
    assert_txt_search_error = '.paging_rowsNumView'

    """ Locators for departments search"""
    Identifier_txt = "tbody tr:nth-child(2) td:nth-child(1)"

    """ Locators for departments ui"""
    ui_txt = '.pages_children'
    menuBar = '.header_title'
