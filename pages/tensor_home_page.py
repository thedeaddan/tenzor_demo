from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorHomePage(BasePage):
    PEOPLE_POWER_SECTION = (By.XPATH, '//*[contains(text(), "Сила в людях")]')
    MORE_DETAILS_LINK = (By.XPATH, '//*[contains(text(), "Подробнее")]')

    def go_to_people_power(self):
        self.click_element(self.PEOPLE_POWER_SECTION)

    def go_to_more_details(self):
        self.click_element(self.MORE_DETAILS_LINK)
