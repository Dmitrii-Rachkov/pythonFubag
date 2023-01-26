from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Welding_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators - локаторы и переменные страницы welding_page

    price_slider_right = "//*[@id='right_slider_c4ca4238a0b923820dcc509a6f75849b']"
    supply_voltage = "//div[@data-property_id='857']"
    checkbox_voltage_220 = "//span[@title='220']"
    apply_filter = "//button[@id='set_filter']"
    product_1 = "//*[@id='bx_3966226736_62777']/div/div[2]/div[1]/div[2]/a"
    all_display = "//div[@class='all_block_nav']"
    add_product_1 = "//*[@id='bx_117848907_62777_basket_actions']/span[1]"
    cart = "//*[@id='headerfixed']/div/div/div/div/div/div/div[3]/div[3]/div/a"

    # Getters - обращение к локаторам welding_page

    def get_price_slider_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_right)))

    def get_supply_voltage(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.supply_voltage)))

    def get_checkbox_voltage_220(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_voltage_220)))

    def get_apply_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_filter)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_all_display(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_display)))

    def get_add_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1)))


    # Actions - действия с нашими локаторами

    def move_price_slider_right(self):
        ActionChains(self.driver).move_to_element(self.get_price_slider_right()).click_and_hold(self.get_price_slider_right()).move_by_offset(-170, 0).release().perform()
        print("Move price slider right")

    def click_supply_voltage(self):
        self.get_supply_voltage().click()
        print("Click supply voltage filter")

    def click_checkbox_voltage_220(self):
        self.get_checkbox_voltage_220().click()
        print("Click checkbox voltage 220")

    def click_apply_filter(self):
        self.get_apply_filter().click()
        print("Click apply filter")

    def click_product_1(self):
        self.get_product_1().click()
        print("Click product_1")

    def click_all_display(self):
        self.get_all_display().click()
        print("Disaplay all products in category")

    def click_add_product_1(self):
        self.get_add_product_1().click()
        self.driver.execute_script("window.scrollTo(0, 800)")
        print("Add to cart product_1")


    # Methods - методы взаимодействия со страницей сварочного оборудования

    def choose_price(self):
        self.move_price_slider_right()
        self.get_screenshot()
        self.get_current_url()

    def choose_supply_voltage(self):
        self.click_supply_voltage()
        self.click_checkbox_voltage_220()
        self.get_screenshot()

    def apply_filter_button(self):
        self.click_apply_filter()
        self.get_screenshot()

    def buy_product_1(self):
        self.click_product_1()
        self.get_current_url()
        self.get_screenshot()
        self.click_add_product_1()

    def display_all_products(self):
        self.click_all_display()

