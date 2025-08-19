from selenium.webdriver.common.by import By


class TransitionLocators:

    #Локатор кнопки "Конструктор"
    BUTTON_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"

    #Локатор кнопки "Личный кабинет"
    BUTTON_ACCOUNT = By.XPATH, ".//a[@href='/account']"

    #Локатор кнопки "Лист заказов"
    BUTTON_LIST_OF_ORDERS = By.XPATH, ".//a[@href='/feed']"
