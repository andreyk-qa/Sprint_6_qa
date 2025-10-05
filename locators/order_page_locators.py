from selenium.webdriver.common.by import By


class OrderPageLocators:

    """
    Локаторы для полей ввода данных
    """
    NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]') # Поле ввода имени
    SURNAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]') # Поле ввода фамилии
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]') # Поле ввода адреса
    METRO_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]') # Поле ввода станции метро
    CHOOSE_METRO = (By.XPATH, ".//div[text()='Черкизовская']") # Выбор станции метро Черкизовская
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]') # Поле ввода телефона
    ORDER_DATE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]') # Поле "Когда привезти самокат"

    """
    Выпадающий список срока аренды
    """
    RENTAL_FIELD = (By.CLASS_NAME, 'Dropdown-arrow') # Кнопка выпадающего списка срока аренды
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, ".//div[text()='сутки']") # Выбор срока на сутки
    RENTAL_PERIOD_TWO_DAY = (By.XPATH, ".//div[text()='двое суток']") # Выбор срока на двое суток

    """
    Цвет самоката
    """
    CHECKBOX_COLOR_BLACK = (By.ID, 'black') # Чекбокс на выбор черного самоката
    CHECKBOX_COLOR_GREY = (By.ID, 'grey') # Чекбокс на выбор черного самоката

    """
    Кнопки формы заказа
    """
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']") # Кнопка Далее
    ORDER_BUTTON = (By.XPATH, ".//button[@class= 'Button_Button__ra12g Button_Middle__1CSJM']") # Кнопка Заказать
    YES_BUTTON = (By.XPATH, ".//button[text()='Да']") # Кнопка "Да" на всплывающем окне "Хотите оформить заказ?"
    VIEW_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")  # Кнопка "Посмотреть статус" на всплывающем окне "Заказ оформлен"

    """
    Логотипы
    """
    LOGO_YANDEX = (By.XPATH, ".//a[@class= 'Header_LogoYandex__3TSOI']") # Логотип Яндекс
    LOGO_SCOOTER = (By.XPATH, ".//a[@class= 'Header_LogoScooter__3lsAR']") # Логотип Самокат

    NEWS_DZEN = (By.XPATH, ".//div[@class= 'dzen-desktop--floor-title__title-2v']") # Новости на Дзен

    ORDER_COMPLETED = (By.XPATH, ".//div[text()='Заказ оформлен']") # Заголовок окна успешного создания заказа