import time

from pages.main_page import Main_page
from pages.welding_page import Welding_page
from utilities.driver import Driver


# В этом тесте купим product_1

def test_1_buy_product_1(set_up, set_group):
    driver = Driver().get_driver()

    # Открываем главную страницу
    mp = Main_page(driver)
    mp.open_main_page()

    # Кликаем фильтр 'сварочное оборудование'
    mp.open_welding_page()

    # Выбираем цену
    wp = Welding_page(driver)
    wp.choose_price()

    # Выбираем параметр напряжения
    wp.choose_supply_voltage()

    # Применяем фильтр
    wp.apply_filter_button()

    # Покупаем product_1
    wp.display_all_products()
    wp.buy_product_1()

    time.sleep(6)
    driver.quit()



