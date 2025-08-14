import config
from pages.base_page import BasePage
from locators.enter_locators import EnterLocators
import allure


class EnterPage(BasePage):

    @allure.step('Проверка отображения страницы входа')
    def check_displaying_enter_page(self):
        return self.check_displaying(EnterLocators.ENTER_PAGE)

    @allure.step('Открытие ссылки на страницу входа')
    def open_url_enter_page(self):
        self.open_url(config.PAGE_LOGIN, EnterLocators.ENTER_PAGE)

    @allure.step('Клик по кнопке-ссылке восстановить пароль')
    def click_to_recovery_url(self):
        self.click_to(EnterLocators.LINK_TO_PASSWORD_RECOVERY)
