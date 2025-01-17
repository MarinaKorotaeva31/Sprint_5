from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestPersonalAccount:
    def test_transfer_to_personal_account(self, driver, open_browser):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(Locators.h_order))  # невидимость заголовка "Соберите заказ"
        current_url = 'https://stellarburgers.nomoreparties.site/account/profile'
        assert driver.current_url == current_url or driver.current_url == 'https://stellarburgers.nomoreparties.site/login'  # для авторизованного и неавторизованного случаев

    def test_transfer_to_constructor(self, driver, open_browser):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(
            Locators.h_order))  # невидимость заголовка "Соберите заказ"
        driver.find_element(*Locators.button_constructor).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.h_order))  # видимость заголовка "Соберите заказ"
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transfer_to_stellar_burgers(self, driver, open_browser):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(
            Locators.h_order))  # невидимость заголовка "Соберите заказ"
        driver.find_element(*Locators.logo_stellar_burger).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.h_order))  # видимость заголовка "Соберите заказ"
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

