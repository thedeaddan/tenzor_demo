from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SbisHomePage(BasePage):
    CONTACTS_LINK = (By.XPATH, '//a[@href="/contacts"]')

    def go_to_contacts(self):
        self.click_element(self.CONTACTS_LINK)
