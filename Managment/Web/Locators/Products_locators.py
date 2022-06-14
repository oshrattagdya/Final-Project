"""Locators for Products screen"""

class ProductsLocators:
    dasbord_products_btn = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[2]/a[2]"
    desc_boxs = "//input[@placeholder='תיאור']"
    product_status_op = "//span[@class='checkbox_checkboxCircle']"



    #stage1
    barcode_field = "//form[1]/div[2]/div[2]/span[1]/div[1]/input[1]"
    product_name_field = "//form[1]/div[2]/div[4]/span[1]/div[1]/input[1]"
    product_price = "//form[1]/div[2]/div[5]/span[1]/div[1]/input[1]"
    date_field = "//input[@placeholder='תאריך תפוגה']"
    desc_field = "//form[1]/div[2]/div[8]/span[1]/div[1]/input[1]"

    #navgation
    next_btn = "//input[@value='הבא']"
    back_btn = "//input[@name='back']"

    #stage2
    cate_btn = "//form[1]/div[2]/div[2]/div[1]/span[1]/div[1]"
    cate_op = "//div[contains(@class,'input_autocompleteItem')][contains(text(),'{}')]"
    store_btn = "//input[@placeholder='חנות']"
    store_op = "//div[@class='input_autocompleteItem '][contains(text(),'{}')]"
    kidom_field = "//input[@placeholder='קידום']"
    kidom_op = "//form[1]/div[2]/div[1]/div[1]/span[1]/div[2]/div[1]/div"

    dep_btn = "//input[@placeholder='מחלקה']"
    dep_auto_op = "//form[1]/div[2]/div[3]/div[1]/span[1]/div[2]/div[1]/div[1]"
    yvoan_makbil = "//form[1]/div[2]/div[6]/span[1]/span[1]"

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


