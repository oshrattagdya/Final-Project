import time
import pytest
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Categories_page import CategoriesPageFunc
from Managment.Web.Utils.utils import Utilitis


@pytest.mark.usefixtures('connect_home_page')
class TestCategories(Base):
    def test_ui_for_categories_page(self):
        driver = self.driver
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        category.click_categories_navbar()
        time.sleep(2)

        util.assertFunc(category.get_ui_categ_page(),"קטגוריות\nהוספה\nייצוא\nמזהה\n\tשם\n\tמחלקות\n\tפעיל\n\tשדות\n\tתאריך יצירה\n\n4jp555dl4e8dzbk\tגרבגרב\tשמפו נגד קשקשים\t✗\tגרב\t\nאתמול, 16:59\n\n4jp555dl4e7ywnf\tגרב\tקוניאק\t✓\tגרב\t\nאתמול, 16:48\n\n4jp555dl4dvbcra\tסוכריה\tקוניאק\t✓\tסוכריה\t\nאתמול, 10:53\n\n4jp555dl4dv8mjt\tפרחים11\tקוניאק\t✓\tפרחים11\t\nאתמול, 10:51\n\n4jp555dl4dv7p45\tפרחים1\tקוניאק\t✓\tפרחים1\t\nאתמול, 10:51\n\n4jp555dl4dunlyr\tפרחים\tקוניאק\t✓\tפרחים\t\nאתמול, 10:35\n\n4jp555dl4du8oz8\tערק11\tקוניאק\t✓\tערק11\t\nאתמול, 10:23\n\n4jp555dl4du78be\tערקי1\tניירות\t✗\tערקי1\t\nאתמול, 10:22\n\n4jp555dl4du6mqf\tערקי\tניירות\t✓\tערקי\t\nאתמול, 10:22\n\n4jp555dl4du26qp\tערקק\tניירות\t✓\tערק\t\nאתמול, 10:18\n\n4jp555dl4dt8rbc\tCC\tנייר\t✓\tFGFG\t\nאתמול, 09:55\n\n4jp555dl4cz8dal\tשמפניה\tקוניאק\t✓\tאוש\t\n13/06/22, 19:55\n\n4jp555dl45pge87\tבירות\tקוניאק\t✓\t1\t\n08/06/22, 17:47\n\npsliag8kpmkdsaq\tחטיפים\tשוקולדים\t✓\tכשרות\t\n07/06/21, 15:02\n\n461hdlknbyuciq\tקנאביס\tבדיקהקנאביס\t✓\t\t\n10/04/21, 19:42\n\nu6z3rgrckkzoqiay\t45645\tבטון\t✓\tfg\t\n10/02/21, 19:06\n\nu6z3r13kkkv9d4hw\tמשקאות\tוודקהקוניאק\t✓\tיבוא מקבילתוצרת הארץ\t\n07/02/21, 16:45\nמציג \n לעמוד\nסה״כ: 17 שורות")