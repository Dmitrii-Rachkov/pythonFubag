from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Driver:

    def get_driver(self):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service_obj = Service('/utilities/chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj, chrome_options=options)
        return driver
