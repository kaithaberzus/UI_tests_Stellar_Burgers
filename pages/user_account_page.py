from pages.base_page import BasePage
from locators.user_account_locators import UserAccountLocators
import allure


class UserAccountPage(BasePage):

    @allure.step('Проверка отображения страницы профиля пользователя')
    def check_displaying_user_account_page(self):
        return self.check_displaying(UserAccountLocators.USER_ACCOUNT_PAGE)

    @allure.step('Клик по кнопке "Выйти')
    def click_to_exit_button(self):
        self.click_to(UserAccountLocators.EXIT_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_to_history_of_orders(self):
        self.click_to(UserAccountLocators.BUTTON_HISTORY_OF_ORDERS)

    @allure.step('Проверка отображения страницы истории заказов')
    def check_displaying_page_history_of_orders(self):
        return self.check_displaying(UserAccountLocators.PAGE_HISTORY_OF_ORDERS)
