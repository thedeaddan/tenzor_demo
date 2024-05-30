from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisContactsPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get("https://sbis.ru/")
        contacts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Контакты"))
        )
        contacts_link.click()

    def click_tensor_banner(self):
        tensor_banner = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='https://tensor.ru/']"))
        )
        tensor_banner.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def select_region(self, region_name):
        region_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".your-region"))
        )
        region_element.click()
        
        region_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".popup-region-selector"))
        )
        
        region_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(),'{region_name}')]"))
        )
        region_link.click()
