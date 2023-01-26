import time

from pages.main_page import Main_page
from pages.welding_page import Welding_page
from utilities.driver import Driver

# В этом тесте проверим, что открывается страница с сварочным оборудованием

def test_1_open_welding_page(set_up, set_group):
    driver = Driver().get_driver()

    # Открываем главную страницу
    mp = Main_page(driver)
    mp.open_main_page()

    # Кликаем фильтр 'сварочное оборудование'
    mp.open_welding_page()

    time.sleep(3)
    driver.quit()

# В этом тесте проверим возможность выбора цены с помощью ползунка

def test_2_choose_price(set_up, set_group):
    driver = Driver().get_driver()

    # Открываем главную страницу
    mp = Main_page(driver)
    mp.open_main_page()

    # Кликаем фильтр 'сварочное оборудование'
    mp.open_welding_page()

    # Выбираем цену
    wp = Welding_page(driver)
    wp.choose_price()

    time.sleep(3)
    driver.quit()

# В этом тесте проверим возможность выбора фильтра напряжение

def test_3_choose_supply_voltage(set_up, set_group):
    driver = Driver().get_driver()

    # Открываем главную страницу
    mp = Main_page(driver)
    mp.open_main_page()

    # Кликаем фильтр 'сварочное оборудование'
    mp.open_welding_page()

    # Выбираем параметр напряжения
    wp = Welding_page(driver)
    wp.choose_supply_voltage()

    time.sleep(3)
    driver.quit()

# В этом тесте выберем все наши фильтры и применим их к странице сварочного оборудования

def test_4_all_filters(set_up, set_group):
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

    time.sleep(6)
    driver.quit()



