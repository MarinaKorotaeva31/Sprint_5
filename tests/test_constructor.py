from locators import Locators

class TestGoToTheSection:
    def test_section_buns(self, driver, open_browser):
        driver.find_element(*Locators.span_sauces).click()  # кликанье на "соусы", чтобы проверить переход к "булкам"
        driver.find_element(*Locators.span_buns).click()
        assert driver.find_element(*Locators.div_buns)  # проверка текущего активного раздела на "Булки"

    def test_section_sauces(self, driver, open_browser):
        driver.find_element(*Locators.span_sauces).click()
        assert driver.find_element(*Locators.div_sauces)

    def test_section_fillings(self, driver, open_browser):
        driver.find_element(*Locators.span_fillings).click()
        assert driver.find_element(*Locators.div_fillings)
