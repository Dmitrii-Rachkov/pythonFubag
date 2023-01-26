import random
import string
import time

from selenium.webdriver.common.by import By

from utilities.driver import Driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = Driver().get_driver()
url = 'https://store.fubag.ru/'
driver.get(url)
driver.maximize_window()
time.sleep(4)

# account = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='auth_wr_inner']")))
# account = driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div/div/div/div[1]/div/div[4]/div/div/a")
# account.click()
# print('click account button')
# time.sleep(4)
#
# registration_button = driver.find_element(By.XPATH, "//*[@id='auth-page-form']/div[2]/div[2]/a")
# registration_button.click()
# time.sleep(3)
#
# page_title = driver.find_element(By.XPATH, "//h1[@id='pagetitle']")
# v_page_title = page_title.text
# assert v_page_title == "Регистрация"
# print("Good page title")
#
# example = ''.join(random.choices(string.ascii_lowercase, k=5)) + "@mail.ru"
# print(f'Например {example}')
#
# intrand = ''.join(random.choices(string.ascii_lowercase, k=5)) + str(random.randint(10000, 99999))
# print(intrand)
# time.sleep(3)
#
# fio = "//label[@for='input_NAME']"
# fio_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, fio)))
# ActionChains(driver).move_to_element(fio_loc).click(fio_loc).perform()
# ActionChains(driver).move_to_element(fio_loc).send_keys("Rambo").perform()
# time.sleep(2)
#
# mail = "//label[@for='input_EMAIL']"
# password = "//label[@for='input_PASSWORD']"
# password_value = ''.join(random.choices(string.ascii_lowercase, k=5)) + str(random.randint(10000, 99999))
# confirm_password = "//label[@for='input_CONFIRM_PASSWORD']"
# reg_button = "//*[@id='registraion-page-form']/div[3]/button"
#
# loc_mail = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, mail)))
# mail_value = ''.join(random.choices(string.ascii_lowercase, k=5)) + "@mail.ru"
# ActionChains(driver).move_to_element(loc_mail).click(loc_mail).perform()
# ActionChains(driver).move_to_element(loc_mail).send_keys(mail_value).perform()
#
# pas_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, password)))
# ActionChains(driver).move_to_element(pas_loc).click(pas_loc).perform()
# ActionChains(driver).move_to_element(pas_loc).send_keys(password_value).perform()
#
# con_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, confirm_password)))
# ActionChains(driver).move_to_element(con_loc).click(con_loc).perform()
# ActionChains(driver).move_to_element(con_loc).send_keys(password_value).perform()
# time.sleep(5)
#
# reg_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, reg_button)))
# ActionChains(driver).move_to_element(reg_loc).click(reg_loc).perform()
# time.sleep(5)
#
# drop = "//*[@id='header']/div[2]/div/div/div/div[1]/div/div[4]/div/div/a/i"
# drop_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, drop)))
# ActionChains(driver).move_to_element(drop_loc).perform()
# time.sleep(3)
#
# exit_button = "//*[@id='header']/div[2]/div/div/div/div[1]/div/div[4]/div/div/ul/li[11]/a/i"
# exit_button_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, exit_button)))
# exit_button_loc.click()
# time.sleep(3)
#
wel = "//*[@id='content']/div/div/div[2]/div/div[1]/ul/li[1]/a"
wel_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, wel)))
wel_loc.click()
time.sleep(3)

slider = "//*[@id='right_slider_c4ca4238a0b923820dcc509a6f75849b']"
slider_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, slider)))
ActionChains(driver).move_to_element(slider_loc).click_and_hold(slider_loc).move_by_offset(-170, 0).release().perform()


time.sleep(3)

supply = "//div[@data-property_id='857']"
supply_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, supply)))
supply_loc.click()
time.sleep(3)

voltage_220 = "//span[@title='220']"
voltage_220_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, voltage_220)))
voltage_220_loc.click()
time.sleep(4)

apply = "//button[@id='set_filter']"
apply_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, apply)))
apply_loc.click()
time.sleep(3)

all_dispaly = "//div[@class='all_block_nav']"
all_dispaly_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, all_dispaly)))
all_dispaly_loc.click()
time.sleep(3)

product_1 = "//*[@id='bx_3966226736_62777']/div/div[2]/div[1]/div[2]/a"
product_1_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, product_1)))
product_1_loc.click()
time.sleep(3)

add_product_1 = "//*[@id='bx_117848907_62777_basket_actions']/span[1]"
add_product_1_loc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, add_product_1)))
add_product_1_loc.click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(5)









