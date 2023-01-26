import random
import string
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Registration_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators - локаторы и переменные страницы registration_page

    fio = "//label[@for='input_NAME']"
    mail = "//label[@for='input_EMAIL']"
    password = "//label[@for='input_PASSWORD']"
    password_value = ''.join(random.choices(string.ascii_lowercase, k=5)) + str(random.randint(10000, 99999))
    confirm_password = "//label[@for='input_CONFIRM_PASSWORD']"
    reg_button = "//*[@id='registraion-page-form']/div[3]/button"

    # Getters - обращение к локаторам registration_page

    def get_fio(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fio)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_confirm_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_password)))

    def get_reg_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reg_button)))


    # Actions - действия с нашими локаторами

    def input_fio(self):
        fio_value = ''.join(random.choices(string.ascii_lowercase, k=5))
        ActionChains(self.driver).move_to_element(self.get_fio()).click(self.get_fio()).perform()
        ActionChains(self.driver).move_to_element(self.get_fio()).send_keys(fio_value).perform()
        print("Input FIO")

    def input_mail(self):
        mail_value = ''.join(random.choices(string.ascii_lowercase, k=5)) + "@mail.ru"
        ActionChains(self.driver).move_to_element(self.get_mail()).click(self.get_mail()).perform()
        ActionChains(self.driver).move_to_element(self.get_mail()).send_keys(mail_value).perform()
        print("Input mail")

    def input_password(self):
        ActionChains(self.driver).move_to_element(self.get_password()).click(self.get_password()).perform()
        ActionChains(self.driver).move_to_element(self.get_password()).send_keys(self.password_value).perform()
        print("Input password")

    def input_confirm_password(self):
        ActionChains(self.driver).move_to_element(self.get_confirm_password()).click(self.get_confirm_password()).perform()
        ActionChains(self.driver).move_to_element(self.get_confirm_password()).send_keys(self.password_value).perform()
        print("Confirm password")

    def click_reg_button(self):
        ActionChains(self.driver).move_to_element(self.get_reg_button()).click(self.get_reg_button()).perform()
        print("Click registration button")


    # Methods - методы взаимодействия со страницей регистрации

    def new_login(self):
        self.input_fio()
        self.input_mail()
        self.input_password()
        self.input_confirm_password()
        self.get_screenshot()
        self.click_reg_button()
        self.get_current_url()
        self.assert_url("https://store.fubag.ru/")

