from sprint_5.locators import Locators
from sprint_5.test_data import TestData
from sprint_5.urls import browser_site, browser_register, browser_login


class TestVerification:

    def test_successful_registration_on_the_main_page(self, driver):
        driver.get(browser_site)
        EMAIL = TestData.EMAIL
        PASSWORD = TestData.PASSWORD

        driver.find_element(*Locators.BUTTON_lOGIN_ACC).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        logout_button = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        assert logout_button.is_displayed(), "Кнопка 'Выход' отображается. Вход выполнен."

    def test_successful_registration_through_your_personal_account(self, driver):
        driver.get(browser_site)
        EMAIL = TestData.EMAIL
        PASSWORD = TestData.PASSWORD

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        logout_button = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        assert logout_button.is_displayed(), "Кнопка 'Выход' отображается. Вход выполнен."

    def test_successful_registration_the_registration_form(self, driver):
        driver.get (browser_register)
        EMAIL = TestData.EMAIL
        PASSWORD = TestData.PASSWORD

        driver.find_element(*Locators.REG_FORM).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        logout_button = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        assert logout_button.is_displayed(), "Кнопка 'Выход' отображается. Вход выполнен."

    def test_successful_registration_the_password_recovery_button(self, driver):
        driver.get(browser_login)
        EMAIL = TestData.EMAIL

        driver.find_element(*Locators.RECOVERY_PASSWORD).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        logout_button = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        assert logout_button.is_displayed(), "Кнопка 'Выход' отображается. Вход выполнен."

