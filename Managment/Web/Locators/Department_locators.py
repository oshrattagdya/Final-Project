""" Locators for department screen"""

class Department_Locators:

    """ Locators for Adding departments"""
    departmet_button = "a:nth-child(24) span:nth-child(2)"
    name_field = "input[placeholder='שם']"
    background_photo = "(//input[contains(@type,'file')])[2]"
    add_button = "input[value='הוספה']"
    activ_button = ".checkbox_checkboxCircle"
    assert_name_txt_Position_1 = "//tbody/tr/td[2]"
    assert_name_txt_Position_2 = "//tbody/tr[2]/td[2]"
    assert_txt_error = "//div[@class='form_note ']"
    assert_txt_search_error = '.paging_rowsNumView'
    assert_img = "imageDiv"

    """ Locators for departments search"""
    Identifier_txt_position2 = "tbody tr:nth-child(2) td:nth-child(1)"

    """ Locators for departments ui"""
    ui_txt = '.pages_children'
    menuBar = '.header_title'
    dropMenu_option_department = "div.dropMenu_option:nth-child({}) > span.dropMenu_text"


    """ Locators for departments Update"""
    update_button = "form_submitBtn"
