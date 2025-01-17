from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from helpers import registration

class TestRegistration:
    def test_registration_success(self, driver, register):
        registration(driver)
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.button_enter))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_password_is_incorrect(self, driver, register):
        driver.find_element(*Locators.input_password).send_keys('vfhjk')
        driver.find_element(*Locators.container_register).click()  # клик по пустому месту для появления сообщения об ошибке
        message = driver.find_element(*Locators.error_message)
        assert message.text == 'Некорректный пароль'
