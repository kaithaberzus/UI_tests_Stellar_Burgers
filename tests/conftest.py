import pytest
import requests
import config
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from data import CompleteData
from data import DRIVER_NAME
from pages.constructor_page import ConstructorPage
from pages.transition import Transition
from pages.user_account_page import UserAccountPage


#Фикстура создания пользователя и его удаления после тестов
@pytest.fixture
def create_user(driver):
    data = CompleteData()
    constructor_page = ConstructorPage(driver)

    data_user = data.body_create_user()

    register = requests.post(f"{config.BASE_URL}{config.USER_URL}/register", data=data_user)
    constructor_page.open_url_constructor_page()
    access_token = register.json().get("accessToken")
    refresh_token = register.json().get("refreshToken")
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')
    constructor_page.open_url_constructor_page()

    yield access_token, data_user
    
    requests.delete(f"{config.BASE_URL}{config.USER_URL}/user", headers={"Authorization": f'{access_token}'})

#Фикстура создания драйвера с вариативным браузером
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        DRIVER_NAME = 'chrome'
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=options)
        DRIVER_NAME = 'firefox'
    yield driver
    driver.quit()

#Фикстура выхода из аккаунта
@pytest.fixture
def exit_from_account(driver, create_user):
    transition = Transition(driver)
    user_page = UserAccountPage(driver)

    transition.click_to_account_button()
    user_page.click_to_exit_button()

    yield