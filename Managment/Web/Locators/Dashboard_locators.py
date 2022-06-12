""" Locators for Dashboard screen"""

class DashboardLocators:
    cupons_button = "//a[@href='#/coupons']//div"
    finnens ="(//a[@class='dashboard_count dashboard_half'])[2]"
    orders = "(//a[contains(@class,'dashboard_count')])[3]"
    products = "(//a[contains(@class,'dashboard_count')])[4]"
    sells = "(//a[contains(@class,'dashboard_count')])[5]"
    stores = "(//a[contains(@class,'dashboard_count')])[6]"
    users = "(//a[contains(@class,'dashboard_count')])[7]"

    allnav = "(//a[contains(@class,'dashboard_count')])[{}]"
    #assert locators
    text = "//main[1]/div[1]/div[1]/span[1]/h4"