from pages.list_of_orders_page import ListOfOrdersPage
from pages.constructor_page import ConstructorPage
from pages.transition import Transition
from pages.base_page import BasePage
from locators.list_of_orders_locators import ListOfOrdersLocators
from helper import Helper
import pytest
import allure



class TestListOfOrdersPage:

    @allure.title('Проверка открытия окна с деталями заказа после клика по заказу на странице ленты заказов')
    def test_window_with_details_open_after_click_to_order(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        list_of_orders_page = ListOfOrdersPage(driver)
        transition = Transition(driver)

        constructor_page.create_order()
        constructor_page.click_to_close_button_order_details_window()
        transition.click_to_list_of_orders_button()
        list_of_orders_page.click_on_last_order()

        assert list_of_orders_page.check_displaying_window_with_order_data(), \
            "Окно с деталями заказа не открылось"

    @allure.title('Проверка отображение заказа из истории заказов в профиле в ленте заказов на странице ленты заказов')
    def test_order_in_history_displayed_in_list_of_orders(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        transition = Transition(driver)
        list_of_orders_page = ListOfOrdersPage(driver)
        base = BasePage(driver)
        helper = Helper()

        order_id = helper.add_reshotka_before_zero(constructor_page.create_order())
        format_order_locator = list_of_orders_page.format_locator_of_order_in_list(order_id)
        constructor_page.click_to_close_button_order_details_window()
        transition.click_to_list_of_orders_button()
        base.scrolling(format_order_locator)

        assert base.check_displaying(format_order_locator), \
            "Заказа из профиля нет в ленте заказов"

    @allure.title('Проверка добавления номера заказа в раздел "В работе" после его создания')
    def test_order_in_progress_after_creation(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        transition = Transition(driver)
        list_of_orders_page = ListOfOrdersPage(driver)
        helper = Helper()

        order_id = helper.add_zero_before_number(constructor_page.create_order())
        constructor_page.click_to_close_button_order_details_window()
        transition.click_to_list_of_orders_button()

        assert order_id in list_of_orders_page.get_text_from_element_orders_in_progress(), \
            "Номера заказа нет в разделе 'В работе'"

    @allure.title('Проверка увеличения счетчиков за все время и за сегодня при создании заказа')
    @pytest.mark.parametrize('counter',
                             [
                                 (ListOfOrdersLocators.COUNTER_FOR_ALL_TIME),
                                 (ListOfOrdersLocators.COUNTER_FOR_TODAY)
                             ]
                             )
    def test_counter_for_all_time_increases(self, driver, create_user, counter):
        list_of_orders_page = ListOfOrdersPage(driver)
        transition = Transition(driver)
        constructor_page = ConstructorPage(driver)
        base = BasePage(driver)

        list_of_orders_page.open_url_of_list_of_orders()
        counter_before = base.get_text_from_element(counter)
        transition.click_to_constructor_button()
        constructor_page.create_order()
        constructor_page.click_to_close_button_order_details_window()
        transition.click_to_list_of_orders_button()
        counter_after = base.get_text_from_element(counter)

        assert counter_after > counter_before, \
            "Счетчик не увеличился"

    @allure.title('Проверка перехода на страницу листа с заказами после клика на кнопку "Лента заказов" в шапке')
    def test_go_to_list_of_orders_page_after_click_to_list_of_orders_button(self, driver):
        transition = Transition(driver)
        list_of_orders_page = ListOfOrdersPage(driver)
        constructor_page = ConstructorPage(driver)

        constructor_page.open_url_constructor_page()
        transition.click_to_list_of_orders_button()

        assert list_of_orders_page.check_list_of_orders_page_displaying(), \
            "Страница ленты заказов не открылась"

