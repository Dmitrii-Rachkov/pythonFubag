from datetime import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')

    """Method assert word"""

    def assert_word(self, actual_word, expected_word):
        value_actual_word = actual_word.text
        assert value_actual_word == expected_word
        print(f'Good value word')

    """Method screenshot"""

    def get_screenshot(self):
        now_date = f'{datetime.now():%Y.%m.%d.%H.%M.%S}'
        name_screenshot = f'screenshot_{now_date}.png'
        self.driver.save_screenshot('D:\\Projects\\pythonFubag\\screen\\' + name_screenshot)
        print(f'Screenshot is done: {name_screenshot}')

    """Method assert URL"""

    def assert_url(self, expected_url):
        get_url = self.driver.current_url
        assert get_url == expected_url
        print("Good value URL")





