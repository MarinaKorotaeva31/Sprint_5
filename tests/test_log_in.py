from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from helpers import log_in, registration


class TestLogIn:
    def test_log_in_to_account_button(self, driver, open_browser):
        driver.find_element(*Locators.button_log_in_to_account).click()
        log_in(driver)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_log_in_personal_account(self, driver, open_browser):
        driver.find_element(*Locators.button_personal_account).click()
        log_in(driver)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_log_in_form_registration(self, driver, register):
        registration(driver)
        driver.find_element(*Locators.button_register).click()
        log_in(driver)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_log_in_recover(self, driver, login_to_account):
        driver.find_element(*Locators.href_recover).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.href_login))
        driver.find_element(*Locators.href_login).click()
        log_in(driver)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
