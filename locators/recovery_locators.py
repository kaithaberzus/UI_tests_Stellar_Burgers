from selenium.webdriver.common.by import By


class RecoveryLocators:

    #Локатор страницы восстановления пароля
    PAGE_RECOVER_PASSWORD = By.XPATH, ".//h2[text()='Восстановление пароля']"

    #Локатор поля ввода почты на странице восстановления пароля
    INPUT_EMAIL_IN_RECOVER_PAGE = By.XPATH, ".//label[text()='Email']/following::input"

    #Локатор кнопки восстановить на первой странице восстановления пароля
    BUTTON_RECOVER = By.XPATH, ".//button[text()='Восстановить']"

    #Локатор поля ввода пароля в активном состоянии
    INPUT_NEW_PASSWORD_OPEN = By.XPATH, './/label[text()="Пароль"]/parent::div[contains(@class, ''"input_status_active")]'

    #Локатор поля ввода кода, как уникальный элемент для второй страницы восстановления пароля
    INPUT_CODE_FROM_LETTER = By.XPATH, ".//label[text()='Введите код из письма']"

    #Локатор значка глаза в поле ввода пароля
    EYE = By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]'
