import random
import string
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def registration(driver):
    email = generate_email()
    password = generate_password()

    name_field = driver.find_element(*Locators.input_name)
    email_field = driver.find_element(*Locators.input_email)
    password_field = driver.find_element(*Locators.input_password)

    name_field.send_keys('Marina')
    email_field.send_keys(email)
    password_field.send_keys(password)

def log_in(driver):
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_enter))
    driver.find_element(*Locators.login).send_keys('Marina_Korotaeva_17_131@gmail.com')
    driver.find_element(*Locators.password).send_keys('gfhjkm')
    driver.find_element(*Locators.button_enter).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_order))

def generate_email(domain='test.ru'):
    user_name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.choice(range(3, 11))))
    return f"{user_name}@{domain}"

def generate_password():
    gen_password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(gen_password, k=random.choice(range(6, 10))))