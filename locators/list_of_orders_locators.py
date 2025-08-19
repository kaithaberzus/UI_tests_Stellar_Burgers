from selenium.webdriver.common.by import By


class ListOfOrdersLocators:

    #Локатор первого сверху заказа в списке заказов на странице списка заказов
    ORDER_IN_LIST_OF_ORDERS = By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]'

    #Локатор окна с данными о первом заказе на странице списка заказов
    MODAL_WINDOW_WITH_ORDER_DATA = By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"

    #Локатор счетчика заказов, сделанных за все время
    COUNTER_FOR_ALL_TIME = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p'

    #Локатор счетчика заказов, сделанных за сегодня
    COUNTER_FOR_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p'

    #Локатор заказа, который находится в процессе подготовки
    ORDER_IN_PROGRESS = By.XPATH, ".//li[@class='text text_type_digits-default mb-2']"

    #Локатор страницы списка заказов
    LIST_OF_ORDERS_PAGE = By.XPATH, ".//h1[text()='Лента заказов']"