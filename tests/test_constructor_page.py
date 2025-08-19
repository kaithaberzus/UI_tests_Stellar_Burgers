from pages.constructor_page import ConstructorPage
from pages.transition import Transition
import allure


class TestConstructorPage:

    @allure.title('Проверка появления окна с информацией об ингредиенте после клика по ингредиенту')
    def test_get_window_with_ingredient_data_after_click_to_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.open_url_constructor_page()
        constructor_page.click_to_ingredient()

        assert constructor_page.check_displaying_window_with_ingredient_data(), \
            "Окно с деталями ингредиента не появилось"

    @allure.title('Проверка перехода на страницу конструктора после клика по кнопке "Конструктор" в шапке')
    def test_go_to_constructor_page_after_click_to_constructor_button(self, driver):
        constructor_page = ConstructorPage(driver)
        transition = Transition(driver)

        constructor_page.open_url_constructor_page()
        transition.click_to_constructor_button()

        assert constructor_page.check_displaying_constructor_page(), \
            "Не произошел переход на страницу конструктора"

    @allure.title('Проверка закрытие окна с информацией об ингредиенте после клика по кнопке-крестику')
    def test_window_with_ingredient_close_after_click_to_close_button(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.open_url_constructor_page()
        constructor_page.click_to_ingredient()
        constructor_page.click_to_close_button_ing_details_window()

        assert constructor_page.check_displaying_constructor_page(), \
            "Окно с деталями ингредиента не закрылось"

    @allure.title('Проверка создание заказа зарегистрированным пользователем')
    def test_auth_user_can_create_order(self, driver, create_user):
        constructor_page = ConstructorPage(driver)

        constructor_page.create_order()

        assert constructor_page.check_displaying_window_with_order_data(), \
            "Окно с деталями созданного заказа не отобразилось"

    @allure.title('Проверка увеличение счетчика ингредиента после добавления его в корзину')
    def test_counter_increases_after_adding_ing_in_basket(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.open_url_constructor_page()
        counter_before = constructor_page.get_text_from_counter()
        constructor_page.drag_and_drop_ingredient()
        counter_after = constructor_page.get_text_from_counter()

        assert counter_after > counter_before, \
            "Счетчик не увеличился"
