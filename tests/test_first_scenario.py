import pytest
from selenium import webdriver
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_first_scenario(driver):
    logger.info("Инит всех страниц")
    sbis_contacts_page = SbisContactsPage(driver)
    tensor_main_page = TensorMainPage(driver)
    tensor_about_page = TensorAboutPage(driver)

    logger.info("Переход на страницу контактов сбиса")
    sbis_contacts_page.go_to_page()

    logger.info("Клик по лого Тензора")
    sbis_contacts_page.click_tensor_banner()

    # Переключаемся на новую вкладку
    logger.info("Переключение на новую вкладку")
    driver.switch_to.window(driver.window_handles[-1])

    logger.info(f"Проверка ссылки, новая ссылка: {driver.current_url}")
    assert driver.current_url == "https://tensor.ru/"

    logger.info("Проверяем есть ли блок 'Сила в людях'")
    assert tensor_main_page.check_block()

    logger.info("Клик по кнопке 'Подробнее'")
    tensor_main_page.click_more()

    logger.info(f"Проверка ссылки, новая ссылка: {driver.current_url}")
    assert driver.current_url == "https://tensor.ru/about"

    logger.info(f"Проверка размера фото")
    assert tensor_about_page.check_working_section_images()
    logger.info(f"Всё ок, заканчиваем")
