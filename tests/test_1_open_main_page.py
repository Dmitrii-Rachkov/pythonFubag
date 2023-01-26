import time

from pages.main_page import Main_page
from utilities.driver import Driver

# Проверим что можем зайти на главную страницу интернет-магазина

def test_open_main_page(set_up, set_group):
    driver = Driver().get_driver()

    # Входим на главную страницу и проверяем URL
    mp = Main_page(driver)
    mp.open_main_page()
    time.sleep(3)
    driver.quit()

