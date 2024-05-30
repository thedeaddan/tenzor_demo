import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from pages.sbis_contacts_page import SbisContactsPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_second_scenario(driver):
    sbis_contacts_page = SbisContactsPage(driver)

    logger.info("Переход на страницу контактов СБИС")
    sbis_contacts_page.go_to_page()

    logger.info("Проверка определения региона")
    region_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"))
    )
    assert region_element.text == "Костромская обл."
    logger.info(f"Регион по умолчанию: {region_element.text}")

    logger.info("Проверка списка партнеров")
    partners_list = driver.find_elements(By.CSS_SELECTOR, ".sbisru-Contacts-List--ellipsis")
    assert len(partners_list) > 0

    logger.info("Изменение региона на Камчатский край")
    region_element.click()

    logger.info("Ожидание появления всплывающего окна выбора региона")
    region_popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".sbis_ru-Region-Panel__header"))
    )
    logger.info("Поиск региона")
    kamchatka_region = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Камчатский край')]"))
    )
    kamchatka_region.click()

    logger.info("Проверка изменения региона на Камчатский край")
    new_region_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"))
    )
    time.sleep(2)
    assert new_region_element.text == "Камчатский край"
    logger.info(f"Выбранный регион: {new_region_element.text}")

    logger.info("Проверка списка партнеров для нового региона")
    new_partners_list = driver.find_elements(By.CSS_SELECTOR, ".sbisru-Contacts-List--ellipsis")
    assert len(new_partners_list) > 0

    logger.info(f"Проверка URL и заголовка страницы: {driver.current_url}, {driver.title}")
    assert "kamchatskij-kraj" in driver.current_url
    assert "Камчатский край" in driver.title
