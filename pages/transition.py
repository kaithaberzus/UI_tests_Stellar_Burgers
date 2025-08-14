from pages.base_page import BasePage
from locators.transition_locators import TransitionLocators
import allure


class Transition(BasePage):

    @allure.step('Клик по кнопке "Конструктор"')
    def click_to_constructor_button(self):
        self.click_to(TransitionLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по кнопке "Лист заказов"')
    def click_to_list_of_orders_button(self):
        self.click_to(TransitionLocators.BUTTON_LIST_OF_ORDERS)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_to_account_button(self):
        self.click_to(TransitionLocators.BUTTON_ACCOUNT)