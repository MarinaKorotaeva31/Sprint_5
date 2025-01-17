Описание проекта:
1. test_registration.py содержит тесты регистрации: test_registration_success (проверка успешной регистрации)
и test_password_is_incorrect (проверка сообщения об ошибки при неверном пароле)
2. test_log_in.py содержит тесты входа: test_log_in_to_account_button (вход по кнопке «Войти в аккаунт» на главной),
test_log_in_personal_account (вход через кнопку «Личный кабинет»), test_log_in_form_registration (вход через кнопку в форме регистрации)
и test_log_in_recover (вход через кнопку в форме восстановления пароля)
3. test_personal_account.py содержит тесты, связанные с личным кабинетом: test_transfer_to_personal_account (переход по кнопке "Личный Кабинет),
test_transfer_to_constructor (переход из ЛК по клику на «Конструктор») и test_transfer_to_stellar_burgers(переход по клику на логотип Stellar Burgers)
4. test_logout.py содержит тест test_log_out_of_account, проверяющий выход из аккаунт
5. test_constructor.py содержит тесты проверки переходов: test_section_buns(к разделу "Булки"), test_section_sauces(к разделу "Соусы"), 
test_section_fillings(к разделу "Начинки")
6. helpers.py содержит вспомогательные функции: registration (функция регистрации), log_in (функция входа в аккаунт), generate_email и generate_password
генерируют почту (логин) и пароль для регистрации соответственно
7. locators.py содержит все используемы локаторы # Sprint_5
