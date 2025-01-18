from sprint_5.helpers.gen_email import generate_email
from sprint_5.locators import Locators
from sprint_5.test_data import TestData


class TestRegistration:

    def test_successful_registration(self, driver_browser_register):
        driver = driver_browser_register
        email = generate_email()
        NAME = TestData.NAME
        PASSWORD = TestData.PASSWORD

        driver.find_element(*Locators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        assert login_button.is_displayed(), "Вход выполнен успешно."

    def test_unsuccessful_registration(self, driver_browser_register):
        email = generate_email()
        driver = driver_browser_register
        NAME = TestData.NAME

        driver.find_element(*Locators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("1")
        driver.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        error_message = driver.find_element(*Locators.ERROR_TEXT).text
        assert "Некорректный пароль" in error_message



