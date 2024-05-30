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
    logger.info(f"Регион: {sbis_contacts_page.get_region()}")
    

    logger.info("Проверка списка партнеров")
    sbis_contacts_page.get_partners()

    logger.info("Изменение региона на Камчатский край")
    sbis_contacts_page.open_region_window()

    logger.info("Смена региона")
    sbis_contacts_page.change_region("Камчатский край")
    logger.info("Проверка изменения региона на Камчатский край")
    logger.info(f"Регион: {sbis_contacts_page.get_region()}")

    logger.info("Проверка списка партнеров для нового региона")
    sbis_contacts_page.get_partners()

    logger.info(f"Проверка URL и заголовка страницы: {driver.current_url}, {driver.title}")
    
