import allure
from pages.enter_page import EnterPage
from pages.password_recovery_page import PasswordRecoveryPage
from data import CompleteData



class TestPasswordRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля при клике по кнопке "Восстановить пароль"')
    def test_check_transfer_to_the_recovery_page_after_click_to_recovery_button(self, driver):
        enter_page = EnterPage(driver)
        recovery_password_page = PasswordRecoveryPage(driver)

        enter_page.open_url_enter_page()
        enter_page.click_to_recovery_url()

        assert recovery_password_page.check_displaying_recovery_password_page(), \
            "Страница восстановления пароля не отобразилась"

    @allure.title('Проверка перехода к странице подтверждения восстановления пароля после введения пароля и нажатия кнопки восстановить')
    def test_fill_email_and_click_on_recovery_button(self, driver, create_user, exit_from_account):
        enter_page = EnterPage(driver)
        recovery_page = PasswordRecoveryPage(driver)
        data = CompleteData()

        enter_page.click_to_recovery_url()
        recovery_page.go_to_the_confirm_recovery_page(data.email_input())

        assert recovery_page.check_displaying_confirmation_of_recovery(), \
            "Страница подтверждения восстановления пароля не отобразилась"

    @allure.title('Проверка подсвечивания поля пароля при нажатии на иконку глаза')
    def test_field_becomes_active_after_click_on_eye(self, driver, create_user, exit_from_account):
        enter_page = EnterPage(driver)
        recovery_page = PasswordRecoveryPage(driver)
        data = CompleteData()

        enter_page.click_to_recovery_url()
        recovery_page.go_to_the_confirm_recovery_page(data.email_input())
        recovery_page.click_to_password_field_eye()

        assert recovery_page.check_displaying_password_open_field(), \
            "Поле пароля не активировалось"