from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorAboutPage(BasePage):
    WORKING_SECTION = (By.XPATH, '//section[contains(@class, "working")]')
    PHOTOS = (By.XPATH, '//section[contains(@class, "working")]//img')

    def get_photo_dimensions(self):
        photos = self.get_elements(self.PHOTOS)
        return [(photo.size['width'], photo.size['height']) for photo in photos]
