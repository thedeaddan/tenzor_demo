from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorAboutPage:
    def __init__(self, driver):
        self.driver = driver

    def check_working_section_images(self):
        images = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tensor_ru-About__block3-image-filter"))
        )
        sizes = [(img.size['width'], img.size['height']) for img in images]
        return all(size == sizes[0] for size in sizes)
