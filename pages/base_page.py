from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from data import DRIVER_NAME


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.stop_time = 10
        self.wait = WebDriverWait(self.driver, self.stop_time)

    @allure.step('Открытие ссылки')
    def open_url(self, url, locator):
        self.driver.get(url)
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            pass

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            pass
        return self.driver.find_element(*locator)

    @allure.step('Клик')
    def click_to(self, locator):
        wait_to = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        click = ActionChains(self.driver)
        click.move_to_element(wait_to).click().perform()

    @allure.step('Заполнение поля')
    def fill_input(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Скролл')
    def scrolling(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Форматирование локатора')
    def format_locator(self, element, value):
        method, locator = element
        locator = locator.format(value)
        return method, locator

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, locator_from, locator_to):
        if DRIVER_NAME == 'chrome':
            self.wait.until(expected_conditions.element_to_be_clickable(locator_from))
            from_element = self.find_element(locator_from)
            to_element = self.find_element(locator_to)
            try:
                self.wait.until(expected_conditions.element_to_be_clickable(locator_from))
                self.wait.until(expected_conditions.element_to_be_clickable(locator_to))
            except TimeoutException:
                pass
            ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()
        else:
            try:
                self.wait.until(expected_conditions.visibility_of_element_located(locator_from))
                self.wait.until(expected_conditions.visibility_of_element_located(locator_to))
            except TimeoutException:
                pass
            element_from = self.driver.find_element(*locator_from)
            element_to = self.driver.find_element(*locator_to)
            self.driver.execute_script(
                """var source = arguments[0];
                var target = arguments[1];
                var evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                source.dispatchEvent(evt);
                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);
                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);
                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);
                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                source.dispatchEvent(evt);
                """, element_from, element_to)

    @allure.step('Закрытие окна')
    def escape(self, locator):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            pass
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()

    @allure.step('Проверка отображение элемента')
    def check_displaying(self, locator):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            pass
        return self.find_element(locator).is_displayed()

    @allure.step('Ожидание исчезновение номер 9999')
    def wait_present_of_text(self, locator):
        try:
            self.wait.until_not(expected_conditions.text_to_be_present_in_element(locator, '9999'))
        except TimeoutException:
            pass