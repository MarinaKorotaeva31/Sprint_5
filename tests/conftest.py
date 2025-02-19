import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from urls import Urls

@pytest.fixture()
def driver():   # фикстура создания драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_browser(driver):  # фикстура открытия главной страницы
    driver.get(Urls.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.logo_stellar_burger))

@pytest.fixture
def login_to_account(driver, open_browser): # фикстура открытия страницы входа
    driver.find_element(*Locators.button_log_in_to_account).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

@pytest.fixture
def register(driver, login_to_account):  # фикстура открытия страницы регистрации
    driver.find_element(*Locators.href_register).click()

