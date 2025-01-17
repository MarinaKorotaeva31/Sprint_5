from selenium.webdriver.common.by import By

class Locators:
    button_log_in_to_account = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    button_enter = (By.XPATH, './/button[text() = "Войти"]')  # кнопка "Войти"
    button_personal_account = (By.XPATH, './/a[@href="/account"]')  # кнопка "Личный Кабинет"
    button_register = (By.XPATH, './/button[text() = "Зарегистрироваться"]')  # кнопка "Зарегистрироваться"
    button_constructor = (By.XPATH, './/p[text()="Конструктор"]')  # кнопка "Конструктор"
    button_exit = (By.XPATH, './/button[text() = "Выход"]')  # кнопка "Выход" в личном кабинете
    button_order = (By.XPATH, './/button[text() = "Оформить заказ"]')  # кнопка "Оформить заказ"

    logo_stellar_burger = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')  # логотип "Stellar Burgers"

    h_order = (By.XPATH, '//h1[text() = "Соберите бургер"]')  # заголовок "Соберите бургер"

    container_register = (By.CLASS_NAME, "App_componentContainer__2JC2W")  # контейнер, используемый для того, чтобы внимание переключилось с поля "пароль" и появилась ошибка неверное введенного пароля

    href_register = (By.CLASS_NAME, "Auth_link__1fOlj")  # гиперссылка "Регистрация"
    href_recover = (By.XPATH, './/a[text()="Восстановить пароль"]')  # гиперссылка "Восстановить пароль"
    href_login = (By.XPATH, './/a[@href="/login"]')

    input_name = (By.XPATH, "//div[contains(., 'Имя')]//input[@name='name']")  # поле "Имя" в форме регистрации
    input_email = (By.XPATH, "//div[contains(., 'Email')]/input")  # поле "Email" в форме регистрации
    input_password = (By.NAME, "Пароль")  # поле "Пароль" в форме регистрации

    login = (By.NAME, "name")  # поле "Email" на странице входа
    password = (By.NAME, "Пароль")  # поле "Пароль" на странице входа

    error_message = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # сообщение об ошибке некорректного пароля

    span_buns = (By.XPATH, "//span[text()='Булки']")  # раздел "Булки"
    span_sauces = (By.XPATH, ".//span[text()='Соусы']")  # раздел "Соусы"
    span_fillings = (By.XPATH, ".//span[text()='Начинки']")  # раздел "Начинки"

    div_buns = (By.XPATH, ".//span[text()='Булки']/parent::div[contains(@class, 'current')]")  # класс активного раздела "Булки"
    div_sauces = (By.XPATH, ".//span[text()='Соусы']/parent::div[contains(@class, 'current')]")  # класс активного раздела "Соусы"
    div_fillings = (By.XPATH, ".//span[text()='Начинки']/parent::div[contains(@class, 'current')]")  # класс активного раздела "Начинки"
