from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage:
    def __init__(self, driver):
        self.driver = driver

    def check_sila_v_lyudyah_block(self):
        sila_v_lyudyah_block = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='tensor_ru-VideoBanner__title']"))
        )
        return sila_v_lyudyah_block is not None

    def click_more(self):
        more_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/about']"))
        )
        more_button.click()
