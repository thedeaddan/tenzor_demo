import pytest
from selenium import webdriver
from pages.sbis_home_page import SbisHomePage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_home_page import TensorHomePage
from pages.tensor_about_page import TensorAboutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_first_scenario(driver):
    sbis_home = SbisHomePage(driver)
    sbis_contacts = SbisContactsPage(driver)
    tensor_home = TensorHomePage(driver)
    tensor_about = TensorAboutPage(driver)

    # 1. Перейти на https://sbis.ru/ в раздел "Контакты"
    driver.get('https://sbis.ru')
    sbis_home.go_to_contacts()

    # 2. Найти баннер Тензор, кликнуть по нему
    sbis_contacts.click_tensor_banner()

    # 3. Перейти на https://tensor.ru/
    driver.switch_to.window(driver.window_handles[1])
    assert 'https://tensor.ru/' in driver.current_url

    # 4. Проверить, что есть блок "Сила в людях"
    assert tensor_home.get_element(tensor_home.PEOPLE_POWER_SECTION) is not None

    # 5. Перейти в этом блоке в "Подробнее" и убедиться, что открывается https://tensor.ru/about
    tensor_home.go_to_more_details()
    assert 'https://tensor.ru/about' in driver.current_url

    # 6. Проверить размеры фотографий в разделе "Работаем"
    photo_dimensions = tensor_about.get_photo_dimensions()
    width, height = photo_dimensions[0]
    for dim in photo_dimensions:
        assert dim == (width, height)

def test_second_scenario(driver):
    sbis_home = SbisHomePage(driver)
    sbis_contacts = SbisContactsPage(driver)

    # 1. Перейти на https://sbis.ru/ в раздел "Контакты"
    driver.get('https://sbis.ru')
    sbis_home.go_to_contacts()

    # 2. Проверить регион и список партнеров
    region = sbis_contacts.get_region()
    assert region == 'Ярославская обл.'
    assert len(sbis_contacts.get_partners_list()) > 0

    # 3. Изменить регион на Камчатский край
    sbis_contacts.set_region('Камчатский край')

    # 4. Проверить новый регион и список партнеров
    assert sbis_contacts.get_region() == 'Камчатский край'
    assert len(sbis_contacts.get_partners_list()) > 0
    assert 'Камчатский край' in driver.title
    assert 'kamchatka' in driver.current_url
