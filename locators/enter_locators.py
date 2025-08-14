from selenium.webdriver.common.by import By


class EnterLocators:

    #Локатор страницы входа в аккаунт
    ENTER_PAGE = By.XPATH, ".//h2[text()='Вход']"

    #Локатор кнопки-ссылки на страницу восстановления пароля
    LINK_TO_PASSWORD_RECOVERY = By.XPATH, ".//a[text()='Восстановить пароль']"