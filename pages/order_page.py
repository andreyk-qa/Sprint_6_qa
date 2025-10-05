from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import Url
import allure


class OrderPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(Url.MAIN_PAGE_URL)
        return self

    @allure.step("Прокрутить до нижней кнопки 'Заказать'")
    def scroll_to_order_big_button(self):
        element = self.wait.until(self.EC.presence_of_element_located(MainPageLocators.ORDER_BIG_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Кликнуть кнопку 'Заказать' вверху страницы")
    def click_order_button_main_page(self):
        self.wait.until(self.EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)).click()

    @allure.step("Кликнуть кнопку 'Заказать' внизу страницы")
    def click_order_big_button_main_page(self):
        self.scroll_to_order_big_button()
        self.wait.until(self.EC.element_to_be_clickable(MainPageLocators.ORDER_BIG_BUTTON)).click()

    @allure.step("Ввести имя: {name}")
    def enter_name(self, name):
        name_field = self.driver.find_element(*OrderPageLocators.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)
        return self

    @allure.step("Ввести фамилию: {surname}")
    def enter_surname(self, surname):
        surname_field = self.driver.find_element(*OrderPageLocators.SURNAME_FIELD)
        surname_field.clear()
        surname_field.send_keys(surname)
        return self

    @allure.step("Ввести адрес: {address}")
    def enter_address(self, address):
        address_field = self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD)
        address_field.clear()
        address_field.send_keys(address)
        return self

    @allure.step("Выбрать станцию метро 'Черкизовская'")
    def enter_metro(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.METRO_FIELD)).click()
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.CHOOSE_METRO)).click()

    @allure.step("Ввести номер телефона: {phone_number}")
    def enter_phone_number(self, phone_number):
        phone_number_field = self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_FIELD)
        phone_number_field.clear()
        phone_number_field.send_keys(phone_number)
        return self

    @allure.step("Кликнуть кнопку 'Далее'")
    def click_next_button(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)).click()

    @allure.step("Ввести дату доставки: {date}")
    def enter_order_date(self, date):
        date_field = self.driver.find_element(*OrderPageLocators.ORDER_DATE_FIELD)
        date_field.send_keys(date)
        return self

    @allure.step("Выбрать срок аренды: сутки")
    def enter_rental_period_one_day(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.RENTAL_FIELD)).click()
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_ONE_DAY)).click()

    @allure.step("Выбрать срок аренды: двое суток")
    def enter_rental_period_two_day(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.RENTAL_FIELD)).click()
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_TWO_DAY)).click()

    @allure.step("Выбрать цвет: черный")
    def click_color_black_checkbox(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.CHECKBOX_COLOR_BLACK)).click()

    @allure.step("Выбрать цвет: серый")
    def click_color_grey_checkbox(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.CHECKBOX_COLOR_GREY)).click()

    @allure.step("Кликнуть кнопку 'Заказать' в форме аренды")
    def click_order_button_order_page(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)).click()

    @allure.step("Кликнуть кнопку 'Да' для подтверждения заказа")
    def click_confirm_button(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.YES_BUTTON)).click()

    @allure.step("Получить текст окна успешного оформления заказа")
    def get_text_completed_order(self):
        return self.wait.until(self.EC.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED)).text

    @allure.step("Кликнуть кнопку 'Посмотреть статус'")
    def click_view_status_button(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.VIEW_STATUS_BUTTON)).click()

    @allure.step("Кликнуть на логотип 'Самокат'")
    def click_logo_scooter(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.LOGO_SCOOTER)).click()

    @allure.step("Кликнуть на логотип 'Яндекс'")
    def click_logo_yandex(self):
        self.wait.until(self.EC.element_to_be_clickable(OrderPageLocators.LOGO_YANDEX)).click()

    @allure.step("Получить текст заголовка главной страницы Самоката")
    def get_text_home_header(self):
        return self.wait.until(self.EC.visibility_of_element_located(MainPageLocators.HOME_HEADER)).text

    @allure.step("Получить текст заголовка страницы Дзена")
    def get_text_news_dzen(self):
        return self.wait.until(self.EC.visibility_of_element_located(OrderPageLocators.NEWS_DZEN)).text

    @allure.step("Переключиться на последнюю открытую вкладку")
    def go_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Сценарий заказа 1 - Шаг 1: Заполнение данных 'Для кого самокат'")
    def order_script_1_step_1(self, name, surname, address, phone_number):
        self.click_order_button_main_page()
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro()
        self.enter_phone_number(phone_number)
        self.click_next_button()
        return self

    @allure.step("Сценарий заказа 1 - Шаг 2: Заполнение данных 'Про аренду'")
    def order_script_1_step_2(self, date):
        self.enter_order_date(date)
        self.enter_rental_period_one_day()
        self.click_color_black_checkbox()
        self.click_order_button_order_page()
        self.click_confirm_button()
        return self

    @allure.step("Сценарий заказа 1 - Шаг 3: Переход на главную страницу через логотип Самоката")
    def order_script_1_step_3(self):
        self.click_view_status_button()
        self.click_logo_scooter()
        return self

    @allure.step("Сценарий заказа 2 - Шаг 1: Заполнение данных 'Для кого самокат'")
    def order_script_2_step_1(self, name, surname, address, phone_number):
        self.scroll_to_order_big_button()
        self.click_order_big_button_main_page()
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro()
        self.enter_phone_number(phone_number)
        self.click_next_button()
        return self

    @allure.step("Сценарий заказа 2 - Шаг 2: Заполнение данных 'Про аренду'")
    def order_script_2_step_2(self, date):
        self.enter_order_date(date)
        self.enter_rental_period_two_day()
        self.click_color_grey_checkbox()
        self.click_order_button_order_page()
        self.click_confirm_button()
        return self

    @allure.step("Сценарий заказа 2 - Шаг 3: Переход на страницу Дзена через логотип Яндекса")
    def order_script_2_step_3(self):
        self.click_view_status_button()
        self.click_logo_yandex()
        self.go_to_last_tab()
        return self
