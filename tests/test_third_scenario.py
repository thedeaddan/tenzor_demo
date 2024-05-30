import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os

import logging

from selenium.webdriver.chrome.options import Options

download_dir = os.path.dirname(os.path.realpath(__file__))

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_third_scenario(driver):
    logger.info("Переход на сайт СБИС")
    driver.get("https://sbis.ru/")


    logger.info("Прокрутка до ссылки 'Скачать локальные версии'")
    download_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Скачать локальные версии"))
    )
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", download_link)
    download_link.click()

    logger.info("Ожидание загрузки страницы с плагинами")
    download_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".sbis_ru-DownloadNew-tabBanner__text"))
    )
    from time import sleep
    sleep(3)
    logger.info("Клик по вкладке 'СБИС Плагин'")
    sbis_plugin_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'СБИС Плагин')]"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(sbis_plugin_tab).click().perform()
    sleep(2)
    logger.info("Поиск всех кнопок с текстом 'Скачать'")
    download_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(text(), 'Скачать (Exe')]"))
    )
    for but in download_buttons:
        logger.info(f"{but.text}")
    
    logger.info("Клик по первой найденной кнопке 'Скачать'")
    download_buttons[0].click()
    site_file_size = float(download_buttons[0].text.split("(")[1].split(" ")[1])
    logger.info(f"Размер файла на сайте: {site_file_size}")

    # Ожидание загрузки файла
    import time
    time.sleep(5)

    files = os.listdir(download_dir)
    downloaded_file = None
    for file in files:
        if "plugin" in file.lower() and file.endswith(".exe"):
            downloaded_file = file
            break

    logger.info(f"Скачанный файл: {downloaded_file}")
    assert downloaded_file is not None, "Файл не был скачан"
    file_size = round(os.path.getsize(os.path.join(download_dir, downloaded_file))/ (1024 * 1024),2)
    logger.info(f"Размер файла: {file_size} Мб")
    os.remove(f"{download_dir}/{downloaded_file}")
    assert file_size == site_file_size, "Размер скачанного файла равен размеру с сайта"
