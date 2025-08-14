from selenium.webdriver.common.by import By


class UserAccountLocators:

    #Локатор кнопки "Выйти"
    EXIT_BUTTON = By.XPATH, './/button[text()="Выход"]'

    #Локатор кнопки "История заказов"
    BUTTON_HISTORY_OF_ORDERS = By.XPATH, './/a[text()="История заказов"]'

    #Локатор страницы личного кабинета
    USER_ACCOUNT_PAGE = By.XPATH, './/p[text()="В этом разделе вы можете изменить свои персональные данные"]'

    #Локатор страницы истории заказов в личном кабинете
    PAGE_HISTORY_OF_ORDERS = By.XPATH, ".//ul[@class='Account_list__3KQQf mb-20']/li/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"

    #Локатор номера заказа из истории заказов с вариативным номером заказа
    VAR_NUMBER_OF_ORDER_IN_HISTORY = By.XPATH, ".//p[@class='text text_type_digits-default' and text()='{}']"