
from conftest import successful_registration_on_the_main_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sprint_5.locators import Locators
from sprint_5.urls import browser_login


class TestLogout:

    def test_logout_button(self, driver, successful_registration_on_the_main_page):
        driver = successful_registration_on_the_main_page

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        logout_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()
        WebDriverWait(driver, 5).until(EC.url_contains(browser_login))
        current_url = driver.current_url
        assert browser_login in current_url, \
            f"Ожидался переход на страницу авторизации, текущий URL: {current_url}"

