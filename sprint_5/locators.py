from selenium.webdriver.common.by import By


class Locators:
    # Заголовок страницы главной
    PAGE_HEADER = (By.XPATH, "//h1[text()='Собери бургер']")

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Поле ввода электронной почты
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")

    # Поле Имя в регистрации
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']:nth-of-type(1)")

    # Поле ввода электронной почты в регистрации
    EMAIL_INPUT_REG = (By.XPATH, "(//input[@name='name'])[2]")

    # Поле ввода пароля
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")

    # Восстановить пароль

    RECOVERY_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")

    # Кнопка подтверждения входа
    CONFIRM_LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")

    # Кнопка "Войти в аккаунт"
    BUTTON_lOGIN_ACC = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")

    # Сообщение об ошибке
    ERROR_TEXT = By.CSS_SELECTOR, ".input__error.text_type_main-default"

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Форма регистрации
    REG_FORM = (By.CSS_SELECTOR, ".Auth_link__1fOlj")

    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # Элемент на главной странице
    SVG_ELEMENT = (By.XPATH, "//*[name()='svg' and @width='290' and @height='50']")

    # Раздел "Соусы" в конструкторе
    SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]")

    # Раздел "Начинки" в конструкторе
    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Начинки']]")

    # Раздел "Булки" в конструкторе
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Булки']]")




