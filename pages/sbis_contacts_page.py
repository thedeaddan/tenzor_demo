from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

    def get_region(self):
        region_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"))
        )
        sleep(2)
        assert region_element.text in ["Костромская обл.","г. Москва","Камчатский край"]
        return region_element
    
    def get_partners(self):
        assert len(self.driver.find_elements(By.CSS_SELECTOR, ".sbisru-Contacts-List--ellipsis")) > 0
    
    def change_region(self,region):
        region_popup = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".sbis_ru-Region-Panel__header"))
    )
        kamchatka_region = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'{region}')]"))
        )
        kamchatka_region.click()

    def open_region_window(self):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"))
        ).click()
    
    def check_url_and_title(self):
        assert "kamchatskij-kraj" in self.driver.current_url
        assert "Камчатский край" in self.driver.title