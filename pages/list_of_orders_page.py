from pages.base_page import BasePage
from locators.list_of_orders_locators import ListOfOrdersLocators
from locators.user_account_locators import UserAccountLocators
import config
import allure


class ListOfOrdersPage(BasePage):

    @allure.step('Клик по крайнему заказу в списке заказов')
    def click_on_last_order(self):
        self.click_to(ListOfOrdersLocators.ORDER_IN_LIST_OF_ORDERS)

    @allure.step('Проверка отображения окна с данными крайнего заказа')
    def check_displaying_window_with_order_data(self):
        return self.check_displaying(ListOfOrdersLocators.MODAL_WINDOW_WITH_ORDER_DATA)

    @allure.step('Преобразование локатора номера заказа')
    def format_locator_of_order_in_list(self, order_id):
        return self.format_locator(UserAccountLocators.VAR_NUMBER_OF_ORDER_IN_HISTORY, order_id)

    @allure.step('Получение текста номера заказа в процессе подготовки')
    def get_text_from_element_orders_in_progress(self):
        return self.get_text_from_element(ListOfOrdersLocators.ORDER_IN_PROGRESS)

    @allure.step('Открытие ссылки страницы ленты заказов')
    def open_url_of_list_of_orders(self):
        self.open_url(config.PAGE_LIST_OF_ORDERS, ListOfOrdersLocators.LIST_OF_ORDERS_PAGE)

    @allure.step('Проверка отображения страницы ленты заказов')
    def check_list_of_orders_page_displaying(self):
        return self.check_displaying(ListOfOrdersLocators.LIST_OF_ORDERS_PAGE)
