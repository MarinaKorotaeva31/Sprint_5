from locators import Locators
from helpers import log_in
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogOut:
    def test_log_out_of_account(self, driver, open_browser):
        driver.find_element(*Locators.button_personal_account).click()
        log_in(driver)
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_exit))
        driver.find_element(*Locators.button_exit).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_enter))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

