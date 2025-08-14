from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
import config
import allure


class ConstructorPage(BasePage):

    @allure.step('Клик по ингредиенту "Краторная булка" в конструкторе')
    def click_to_ingredient(self):
        self.click_to(ConstructorLocators.INGREDIENT_CRATORNAIA_BULKA)

    @allure.step('Проверка отображения окна с информацией об ингредиенте')
    def check_displaying_window_with_ingredient_data(self):
        return self.check_displaying(ConstructorLocators.WINDOW_WITH_ING_DATA)

    @allure.step('Проверка отображения страницы конструктора')
    def check_displaying_constructor_page(self):
        return self.check_displaying(ConstructorLocators.CONSTRUCTOR_PAGE)

    @allure.step('Открытие ссылки на страницу конструктора')
    def open_url_constructor_page(self):
        self.open_url(config.PAGE_CONSTRUCTOR,ConstructorLocators.CONSTRUCTOR_PAGE)

    @allure.step('Перетаскивание ингредиента в корзину')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop(ConstructorLocators.INGREDIENT_CRATORNAIA_BULKA, ConstructorLocators.BASKET)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_to_create_order_button(self):
        self.click_to(ConstructorLocators.BUTTON_CREATE_ORDER)

    @allure.step('Проверка отображения окна с деталями оформленного заказа')
    def check_displaying_window_with_order_data(self):
        return self.check_displaying(ConstructorLocators.WINDOW_WITH_ORDER_DATA)

    @allure.step('Получение текста элемента счетчика ингредиента "Краторная булка')
    def get_text_from_counter(self):
        return self.get_text_from_element(ConstructorLocators.COUNTER)

    @allure.step('Закрытие окна с информацией ою ингредиенте')
    def click_to_close_button_ing_details_window(self):
        self.escape(ConstructorLocators.WINDOW_WITH_ING_DATA)

    @allure.step('Закрытие окна с деталями заказа')
    def click_to_close_button_order_details_window(self):
        self.escape(ConstructorLocators.WINDOW_WITH_ORDER_DATA)

    @allure.step('Проверка отображения кнопки "Оформить заказ"')
    def check_displaying_create_order_button(self):
        return self.check_displaying(ConstructorLocators.BUTTON_CREATE_ORDER)

    @allure.step('Создание заказа')
    def create_order(self):
        self.drag_and_drop_ingredient()
        self.click_to_create_order_button()
        self.wait_present_of_text(ConstructorLocators.ORDER_NUMBER)
        order_id = self.get_text_from_element(ConstructorLocators.ORDER_NUMBER)
        return order_id
