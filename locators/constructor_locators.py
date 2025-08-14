from selenium.webdriver.common.by import By


class ConstructorLocators:

    #Локатор ингредиента "Краторная булка"
    INGREDIENT_CRATORNAIA_BULKA = By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'

    #Локатор кнопки-крестика окна деталей об ингредиенте
    CLOSE_BUTTON = By.CLASS_NAME, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"

    #Локатор корзины
    BASKET = By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']"

    #Локатор счетчика ингредиента "Краторная булка"
    COUNTER = By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']/div[@class='counter_counter__ZNLkj counter_default__28sqi']"

    #Локатор кнопки создания заказа
    BUTTON_CREATE_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'

    #Локатор окна с деталями об ингредиенте
    WINDOW_WITH_ING_DATA = By.XPATH, ".//h2[text()='Детали ингредиента']"

    #Локатор окна с информацией о заказе
    WINDOW_WITH_ORDER_DATA = By.XPATH, ".//p[text()='идентификатор заказа']"

    #Локатор страницы конструктора
    CONSTRUCTOR_PAGE = By.XPATH, ".//h1[text()='Соберите бургер']"

    #Локатор номера заказа в окне с информацией о заказе
    ORDER_NUMBER = By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"