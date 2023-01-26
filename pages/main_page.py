from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):

    url = 'https://store.fubag.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators - локаторы страницы main_page

    account_button = "//*[@id='header']/div[2]/div/div/div/div[1]/div/div[4]/div/div/a"
    registration_button = "//*[@id='auth-page-form']/div[2]/div[2]/a"
    page_title = "//h1[@id='pagetitle']"
    account_down = "//*[@id='header']/div[2]/div/div/div/div[1]/div/div[4]/div/div/a/i"
    exit_button = "//*[@id='header']/div[2]/div/div/div/div[1]/div/div[4]/div/div/ul/li[11]/a/i"
    welding_filter = "//*[@id='content']/div/div/div[2]/div/div[1]/ul/li[1]/a"


    # Getters - обращение к локаторам main_page

    def get_account_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_registration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_button)))

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_account_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_exit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exit_button)))

    def get_welding_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.welding_filter)))


    # Actions - действия с нашими локаторами

    def click_account_button(self):
        self.get_account_button().click()
        print("Click my account button")

    def click_registration_button(self):
        self.get_registration_button().click()
        print("Click registration button")

    def hover_account_down(self):
        ActionChains(self.driver).move_to_element(self.get_account_down()).perform()

    def click_exit_button(self):
        self.get_exit_button().click()
        print("Click exit button")

    def click_welding_filter(self):
        self.get_welding_filter().click()
        print("Click welding filter")


    # Methods - методы взаимодействия со страницей

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_url("https://store.fubag.ru/")

    def registration_form(self):
        self.click_account_button()
        self.click_registration_button()
        self.get_current_url()
        self.get_screenshot()
        self.assert_word(self.get_page_title(), "Регистрация")

    def unregistration(self):
        self.hover_account_down()
        self.click_exit_button()
        self.get_current_url()

    def open_welding_page(self):
        self.click_welding_filter()
        self.get_current_url()
        self.get_screenshot()
        self.assert_url("https://store.fubag.ru/catalog/svarochnoe-oborudovanie/")

