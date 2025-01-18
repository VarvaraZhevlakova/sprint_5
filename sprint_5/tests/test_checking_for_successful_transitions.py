
from conftest import successful_registration_on_the_main_page
from sprint_5.locators import Locators


class TestNavigation:

    def test_transfer_to_personal_account(self, driver_browser_site):
        driver = driver_browser_site

        current_url_before = driver.current_url
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        current_url_after = driver.current_url
        assert current_url_before != current_url_after, "URL изменился после клика на URL 'Личный Кабинет'"

    def test_switching_to_the_constructor(self, driver_browser_site, successful_registration_on_the_main_page):
        driver = driver_browser_site

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        current_url_before = driver.current_url
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        current_url_after = driver.current_url
        assert current_url_before != current_url_after, "URL изменился после клика на 'Конструктор'"

    def test_switching_to_the_logo(self, driver_browser_site, successful_registration_on_the_main_page):
        driver = driver_browser_site

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        svg_element = driver.find_element(*Locators.SVG_ELEMENT)
        assert svg_element is not None, "SVG элемент найден"

