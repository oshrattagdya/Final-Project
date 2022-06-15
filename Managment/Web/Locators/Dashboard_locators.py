""" Locators for Dashboard screen"""

class DashboardLocators:
    #navbar button up
    cupons_button = "//a[@href='#/coupons']//div"
    finnens ="(//a[@class='dashboard_count dashboard_half'])[2]"
    orders = "(//a[contains(@class,'dashboard_count')])[3]"
    products = "(//a[contains(@class,'dashboard_count')])[4]"
    sells = "(//a[contains(@class,'dashboard_count')])[5]"
    stores = "(//a[contains(@class,'dashboard_count')])[6]"
    users = "(//a[contains(@class,'dashboard_count')])[7]"

    allnav = "(//a[contains(@class,'dashboard_count')])[{}]"
    graf = "//canvas[@class='chartjs-render-monitor']"

    #assert locators
    text = "span[class='header_title'] h4"

    # ui locators
    avg_sum = "//div[@class='dashboard_pieData']//div[1]//*[name()='svg']//*[name()='g' and contains(@class,'undefined ')]//*[name()='text' and contains(@y,'50%')]//*[name()='tspan' and contains(@class,'donutChart')]"
    order_sum = "//div[@class='dashboard_pieData']//div[2]//*[name()='svg']//*[name()='g' and contains(@class,'undefined ')]//*[name()='text' and contains(@y,'50%')]//*[name()='tspan' and contains(@class,'donutChart')]"
