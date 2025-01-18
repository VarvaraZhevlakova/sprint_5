from sprint_5.locators import Locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTabs:

    def test_transfer_to_personal_toppings(self, driver_browser_site):
        driver = driver_browser_site

        driver.find_element(*Locators.FILLINGS_SECTION).click()
        driver.find_element(*Locators.FILLINGS_ELEMENT)
        image_element = driver.find_element(*Locators.FILLINGS_PIC)
        image_element.click()
        modal_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.CLASS)
        )
        assert modal_element.is_displayed(), "Новый элемент начинки отображается на странице"
        ingredient_text = driver.find_element(*Locators.FILLINGS_ELEMENT)
        assert ingredient_text.text == "Филе Люминесцентного тетраодонтимформа", \
            f"Ожидался текст 'Филе Люминесцентного тетраодонтимформа', '{ingredient_text.text}'"
        close_button = driver.find_element(*Locators.CLOSE)
        close_button.click()

    def test_transfer_to_personal_sauces(self, driver_browser_site):
        driver = driver_browser_site

        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.SAUCES_ELEMENT)
        image_element = driver.find_element(*Locators.SAUCES_PIC)
        image_element.click()
        modal_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.CLASS)
        )
        assert modal_element.is_displayed(), "Новый элемент соуса отображается на странице"
        ingredient_text = driver.find_element(*Locators.SAUCES_ELEMENT)
        assert ingredient_text.text == "Соус фирменный Space Sauce", \
            f"Ожидался текст 'Соус фирменный Space Sauce', '{ingredient_text.text}'"
        close_button = driver.find_element(*Locators.CLOSE)
        close_button.click()

    def test_transfer_to_personal_bread(self, driver_browser_site):
        driver = driver_browser_site

        bun_image = driver.find_element(*Locators.VIOLET_BUNS)
        driver.execute_script("arguments[0].click();", bun_image)
        modal_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.CLASS)
        )
        assert modal_element.is_displayed(), "Окно с деталями ингредиента открылось"
        ingredient_text = driver.find_element(*Locators.BUNS_ING)
        assert ingredient_text.text == "Флюоресцентная булка R2-D3", \
            f"Ожидался текст 'Флюоресцентная булка R2-D3', '{ingredient_text.text}'"
        close_button = driver.find_element(*Locators.CLOSE)
        close_button.click()













