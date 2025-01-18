import pytest
from selenium import webdriver

from sprint_5.test_data import TestData
from sprint_5.locators import Locators
from sprint_5.urls import browser_site, browser_profile, browser_register, browser_login


@pytest.fixture
def driver_browser_site():
    driver = webdriver.Chrome()
    driver.get(browser_site)
    yield driver
    driver.quit()


@pytest.fixture
def driver_browser_profile():
    driver = webdriver.Chrome()
    driver.get(browser_profile)
    yield driver
    driver.quit()


@pytest.fixture
def driver_browser_register():
    driver = webdriver.Chrome()
    driver.get(browser_register)
    yield driver
    driver.quit()


@pytest.fixture
def driver_browser_login():
    driver = webdriver.Chrome()
    driver.get(browser_login)
    yield driver
    driver.quit()


@pytest.fixture
def successful_registration_on_the_main_page(driver):
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
    driver.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
    driver.quit()



