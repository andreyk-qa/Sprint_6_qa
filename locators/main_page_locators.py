from selenium.webdriver.common.by import By


class MainPageLocators:

    """
    Локаторы выпадающего списка 'Вопросы о важном'
    """
    DROP_LIST_QUESTIONS_1_HEADING = (By.ID, "accordion__heading-0") # Вопрос выпадающего списка "Вопросы о важном" - Сколько это стоит? И как оплатить?
    DROP_LIST_QUESTIONS_1_PANEL = (By.XPATH, ".//*[@id='accordion__panel-0']//p") # Ответ выпадающего списка "Вопросы о важном" - Сколько это стоит? И как оплатить?
    DROP_LIST_QUESTIONS_2_HEADING = (By.ID, "accordion__heading-1") # Вопрос выпадающего списка "Вопросы о важном" - Хочу сразу несколько самокатов! Так можно?
    DROP_LIST_QUESTIONS_2_PANEL = (By.XPATH, ".//*[@id='accordion__panel-1']//p") # Ответ выпадающего списка "Вопросы о важном" - Хочу сразу несколько самокатов! Так можно?
    DROP_LIST_QUESTIONS_3_HEADING = (By.ID, "accordion__heading-2") # Вопрос выпадающего списка "Вопросы о важном" - Как рассчитывается время аренды?
    DROP_LIST_QUESTIONS_3_PANEL = (By.XPATH, ".//*[@id='accordion__panel-2']//p") # Ответ выпадающего списка "Вопросы о важном" - Как рассчитывается время аренды?
    DROP_LIST_QUESTIONS_4_HEADING = (By.ID, "accordion__heading-3") # Вопрос выпадающего списка "Вопросы о важном" - Можно ли заказать самокат прямо на сегодня?
    DROP_LIST_QUESTIONS_4_PANEL = (By.XPATH, ".//*[@id='accordion__panel-3']//p") # Ответ выпадающего списка "Вопросы о важном" - Можно ли заказать самокат прямо на сегодня?
    DROP_LIST_QUESTIONS_5_HEADING = (By.ID, "accordion__heading-4") # Вопрос выпадающего списка "Вопросы о важном" - Можно ли продлить заказ или вернуть самокат раньше?
    DROP_LIST_QUESTIONS_5_PANEL = (By.XPATH, ".//*[@id='accordion__panel-4']//p") # Ответ выпадающего списка "Вопросы о важном" - Можно ли продлить заказ или вернуть самокат раньше?
    DROP_LIST_QUESTIONS_6_HEADING = (By.ID, "accordion__heading-5") # Вопрос выпадающего списка "Вопросы о важном" - Вы привозите зарядку вместе с самокатом?
    DROP_LIST_QUESTIONS_6_PANEL = (By.XPATH, ".//*[@id='accordion__panel-5']//p") # Ответ выпадающего списка "Вопросы о важном" - Вы привозите зарядку вместе с самокатом?
    DROP_LIST_QUESTIONS_7_HEADING = (By.ID, "accordion__heading-6") # Вопрос выпадающего списка "Вопросы о важном" - Можно ли отменить заказ?
    DROP_LIST_QUESTIONS_7_PANEL = (By.XPATH, ".//*[@id='accordion__panel-6']//p") # Ответ выпадающего списка "Вопросы о важном" - Можно ли отменить заказ?
    DROP_LIST_QUESTIONS_8_HEADING = (By.ID, "accordion__heading-7") # Вопрос выпадающего списка "Вопросы о важном" - Я жизу за МКАДом, привезёте?
    DROP_LIST_QUESTIONS_8_PANEL = (By.XPATH, ".//*[@id='accordion__panel-7']//p") # Ответ выпадающего списка "Вопросы о важном" - Я жизу за МКАДом, привезёте?

    """
    Локаторы кнопки 'Заказать'
    """
    ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g") # Кнопка "Заказать" вверху главной страницы
    ORDER_BIG_BUTTON = (By.CLASS_NAME, "Home_FinishButton__1_cWm") # Кнопка "Заказать" внизу главной страницы

    HOME_HEADER = (By.CLASS_NAME, "Home_Header__iJKdX")  # Заголовок "Самокат" на главной странице