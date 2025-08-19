from pages.user_account_page import UserAccountPage
from pages.transition import Transition
from pages.enter_page import EnterPage
import allure


class TestUserAccount:

    @allure.title('Проверка перехода на страницу истории заказов в профиле')
    def test_transition_to_history_of_orders(self, driver, create_user):
        transition = Transition(driver)
        user_page = UserAccountPage(driver)

        transition.click_to_account_button()
        user_page.click_to_history_of_orders()

        assert user_page.check_displaying_page_history_of_orders(), \
            "История заказов в профиле не отобразилась"

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_account(self, driver, create_user):
        transition = Transition(driver)
        user_page = UserAccountPage(driver)
        enter_page = EnterPage(driver)

        transition.click_to_account_button()
        user_page.click_to_exit_button()

        assert enter_page.check_displaying_enter_page(), \
            "Не отобразилась страница входа в аккаунт"

    @allure.title('Проверка перехода на страницу аккаунта пользователя при клике по кнопке "Личный кабинет" для залогиненого пользователя')
    def test_go_to_user_account_cabinet(self, driver, create_user):
        transition = Transition(driver)
        user_page = UserAccountPage(driver)

        transition.click_to_account_button()

        assert user_page.check_displaying_user_account_page(), \
            "Не отобразилась страница профиля пользователя"