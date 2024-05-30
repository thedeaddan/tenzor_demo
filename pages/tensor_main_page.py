from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage:
    def __init__(self, driver):
        self.driver = driver

    def check_block(self):
        block = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class='tensor_ru-Index__card-title tensor_ru-pb-16']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", block)
        return block is not None

    def click_more(self):
        more_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/about']"))
        )
        more_button.click()
