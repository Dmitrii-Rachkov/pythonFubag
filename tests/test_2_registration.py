import time

from pages.main_page import Main_page
from pages.registration_page import Registration_page
from utilities.driver import Driver

# В этом тесте проверим что можем открыть форму регистрации

def test_open_registration_form(set_up, set_group):
    driver = Driver().get_driver()

    # Открываем главную страницу
    mp = Main_page(driver)
    mp.open_main_page()

    # Нажимаем кнопку регистрация
    mp.registration_form()

    time.sleep(3)
    driver.quit()

# В этом тесте мы регистрируемся как новый пользователь

def test_registration(set_up, set_group):
    driver = Driver().get_driver()

    # Открываем главную страницу
    mp = Main_page(driver)
    mp.open_main_page()

    # Нажимаем кнопку регистрация
    mp.registration_form()

    # Заполняем форму регистрации и жмём зарегистрироваться
    rp = Registration_page(driver)
    rp.new_login()

    time.sleep(3)
    driver.quit()

# В этом тесте мы разлогиниваемся

def test_unregistration(set_up, set_group):
    driver = Driver().get_driver()

    # Открываем главную страницу
    mp = Main_page(driver)
    mp.open_main_page()

    # Нажимаем кнопку регистрация
    mp.registration_form()

    # Заполняем форму регистрации и жмём зарегистрироваться
    rp = Registration_page(driver)
    rp.new_login()

    # Жмём кнопку выйти из личного кабинета
    mp.unregistration()

    time.sleep(3)
    driver.quit()








