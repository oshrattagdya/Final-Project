"""Locators for Products screen"""

class ProductsLocators:
    dasbord_products_btn = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[2]/a[2]"
    desc_boxs = "//input[@placeholder='תיאור']"
    product_status_op = "//span[@class='checkbox_checkboxCircle']"



    #stage1
    barcode_field = "input[placeholder='ברקוד']"
    product_name_field = "input[placeholder='שם']"
    product_price = "input[placeholder='מחיר']"
    date_field = "input[placeholder='תאריך תפוגה']"


    #navgation
    next_btn = "//input[@value='הבא']"
    back_btn = "//input[@name='back']"

    #stage2
    cate_btn = "input[placeholder='קטגוריה על']"
    cate_op = "//div[contains(@class,'input_autocompleteItem')][contains(text(),'{}')]"
    store_btn = "input[placeholder='חנות']"
    store_op = "//div[@class='input_autocompleteItem '][contains(text(),'{}')]"
    kidom_field = "//input[@placeholder='קידום']"
    kidom_op = "//form[1]/div[2]/div[1]/div[1]/span[1]/div[2]/div[1]/div"

    dep_btn = "//input[@placeholder='מחלקה']"
    dep_auto_op = "//form[1]/div[2]/div[3]/div[1]/span[1]/div[2]/div[1]/div[1]"
    yvoan_makbil = "(//span[contains(@class,'checkbox_checkboxCircle')])[2]"

    #stage3
    wight_btn = "//form[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]"
    wight_avg_per_unit_field = "//input[@placeholder='משקל ממוצע ליח׳']"
    wight_unit_scale_btn = "//input[@placeholder='יחידת מידה']"
    scale_op = "//div[contains(text(),'{}')]"
    boxes_amout_field = "//input[contains(@placeholder,'יחידות בקרטון')]"
    amout_field = "//input[@placeholder='כמות']"
    min_amout_field = "//input[@placeholder='מינימום קרטונים להזמנה']"

    #stage4
    city_field = "//input[contains(@placeholder,'עיר')]"
    street_field = "//input[@placeholder='רחוב']"
    home_num_field = "//input[@placeholder='מספר']"
    contact_num_field = "//input[@placeholder='contactNumber']"


