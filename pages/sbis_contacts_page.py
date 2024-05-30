from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SbisContactsPage(BasePage):
    TENSOR_BANNER = (By.XPATH, '//img[@alt="Тензор"]')
    REGION_FIELD = (By.XPATH, '//*[contains(@class, "region-select")]')
    PARTNERS_LIST = (By.XPATH, '//*[contains(@class, "partners-list")]')
    REGION_INPUT = (By.XPATH, '//*[@placeholder="Регион"]')

    def click_tensor_banner(self):
        self.click_element(self.TENSOR_BANNER)

    def get_region(self):
        return self.get_element(self.REGION_FIELD).text

    def set_region(self, region):
        region_input = self.get_element(self.REGION_INPUT)
        region_input.clear()
        region_input.send_keys(region)

    def get_partners_list(self):
        return self.get_elements(self.PARTNERS_LIST)
