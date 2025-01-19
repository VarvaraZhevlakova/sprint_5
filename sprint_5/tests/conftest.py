import pytest
from selenium import webdriver

from sprint_5.test_data import TestData
from sprint_5.locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def successful_registration_on_the_main_page(driver):
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
    driver.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()



