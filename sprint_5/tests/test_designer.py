from sprint_5.locators import Locators
from sprint_5.urls import browser_site


class TestTabs:

    def test_transfer_to_personal_toppings(self, driver):
        driver.get(browser_site)

        fillings_section = driver.find_element(*Locators.FILLINGS_SECTION)
        fillings_section.click()
        current_class = fillings_section.get_attribute('class')
        assert "tab_tab_type_current__2BEPc" in current_class, \
            f"Ожидался класс 'tab_tab_type_current__2BEPc', '{current_class}'"

    def test_transfer_to_personal_sauces(self, driver):
        driver.get(browser_site)

        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        current_class = sauces_section.get_attribute('class')
        assert "tab_tab_type_current__2BEPc" in current_class, \
            f"Ожидался класс 'tab_tab_type_current__2BEPc', '{current_class}'"

    def test_transfer_to_personal_bread(self, driver):
        driver.get(browser_site)

        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        buns_section = driver.find_element(*Locators.BUNS_SECTION)
        buns_section.click()
        current_class = buns_section.get_attribute('class')
        assert "tab_tab_type_current__2BEPc" in current_class, \
            f"Ожидался класс 'tab_tab_type_current__2BEPc', '{current_class}'"














