from pages.base_page import BasePage
from locators.recovery_locators import RecoveryLocators
import allure


class PasswordRecoveryPage(BasePage):

    @allure.step('Проверка отображения страницы восстановления пароля')
    def check_displaying_recovery_password_page(self):
        return self.check_displaying(RecoveryLocators.PAGE_RECOVER_PASSWORD)

    @allure.step('Заполнение поля почты на странице восстановления пароля')
    def fill_email_input(self, email):
        self.fill_input(RecoveryLocators.INPUT_EMAIL_IN_RECOVER_PAGE, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_to_the_button_recovery(self):
        self.click_to(RecoveryLocators.BUTTON_RECOVER)

    @allure.step('Проверка отображения второй страницы-подтверждения восстановления пароля')
    def check_displaying_confirmation_of_recovery(self):
        return self.check_displaying(RecoveryLocators.INPUT_CODE_FROM_LETTER)

    @allure.step('Клик по иконке глаза в поле пароля')
    def click_to_password_field_eye(self):
        self.click_to(RecoveryLocators.EYE)

    @allure.step('Проверка отображения активного поля пароля')
    def check_displaying_password_open_field(self):
        return self.check_displaying(RecoveryLocators.INPUT_NEW_PASSWORD_OPEN)

    @allure.step('Переход на страницу восстановления пароля')
    def go_to_the_confirm_recovery_page(self, email):
        self.fill_email_input(email)
        self.click_to_the_button_recovery()

