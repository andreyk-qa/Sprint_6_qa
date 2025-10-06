from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import Url
import allure


class OrderPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self._open_url(Url.MAIN_PAGE_URL)
        return self

    @allure.step("Прокрутить до нижней кнопки 'Заказать'")
    def scroll_to_order_big_button(self):
        self._scroll_to_element(MainPageLocators.ORDER_BIG_BUTTON)

    @allure.step("Кликнуть кнопку 'Заказать' вверху страницы")
    def click_order_button_main_page(self):
        self._click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Кликнуть кнопку 'Заказать' внизу страницы")
    def click_order_big_button_main_page(self):
        self.scroll_to_order_big_button()
        self._click(MainPageLocators.ORDER_BIG_BUTTON)

    @allure.step("Ввести имя: {name}")
    def enter_name(self, name):
        self._send_keys(OrderPageLocators.NAME_FIELD, name)
        return self

    @allure.step("Ввести фамилию: {surname}")
    def enter_surname(self, surname):
        self._send_keys(OrderPageLocators.SURNAME_FIELD, surname)
        return self

    @allure.step("Ввести адрес: {address}")
    def enter_address(self, address):
        self._send_keys(OrderPageLocators.ADDRESS_FIELD, address)
        return self

    @allure.step("Выбрать станцию метро 'Черкизовская'")
    def enter_metro(self):
        self._click(OrderPageLocators.METRO_FIELD)
        self._click(OrderPageLocators.CHOOSE_METRO)

    @allure.step("Ввести номер телефона: {phone_number}")
    def enter_phone_number(self, phone_number):
        self._send_keys(OrderPageLocators.PHONE_NUMBER_FIELD, phone_number)
        return self

    @allure.step("Кликнуть кнопку 'Далее'")
    def click_next_button(self):
        self._click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Ввести дату доставки: {date}")
    def enter_order_date(self, date):
        self._find_element(OrderPageLocators.ORDER_DATE_FIELD).send_keys(date)
        return self

    @allure.step("Выбрать срок аренды: сутки")
    def enter_rental_period_one_day(self):
        self._click(OrderPageLocators.RENTAL_FIELD)
        self._click(OrderPageLocators.RENTAL_PERIOD_ONE_DAY)

    @allure.step("Выбрать срок аренды: двое суток")
    def enter_rental_period_two_day(self):
        self._click(OrderPageLocators.RENTAL_FIELD)
        self._click(OrderPageLocators.RENTAL_PERIOD_TWO_DAY)

    @allure.step("Выбрать цвет: черный")
    def click_color_black_checkbox(self):
        self._click(OrderPageLocators.CHECKBOX_COLOR_BLACK)

    @allure.step("Выбрать цвет: серый")
    def click_color_grey_checkbox(self):
        self._click(OrderPageLocators.CHECKBOX_COLOR_GREY)

    @allure.step("Кликнуть кнопку 'Заказать' в форме аренды")
    def click_order_button_order_page(self):
        self._click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Кликнуть кнопку 'Да' для подтверждения заказа")
    def click_confirm_button(self):
        self._click(OrderPageLocators.YES_BUTTON)

    @allure.step("Получить текст окна успешного оформления заказа")
    def get_text_completed_order(self):
        return self._get_text(OrderPageLocators.ORDER_COMPLETED)

    @allure.step("Кликнуть кнопку 'Посмотреть статус'")
    def click_view_status_button(self):
        self._click(OrderPageLocators.VIEW_STATUS_BUTTON)

    @allure.step("Кликнуть на логотип 'Самокат'")
    def click_logo_scooter(self):
        self._click(OrderPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип 'Яндекс'")
    def click_logo_yandex(self):
        self._click(OrderPageLocators.LOGO_YANDEX)

    @allure.step("Получить текст заголовка главной страницы Самоката")
    def get_text_home_header(self):
        return self._get_text(MainPageLocators.HOME_HEADER)

    @allure.step("Получить текст заголовка страницы Дзена")
    def get_text_news_dzen(self):
        return self._get_text(OrderPageLocators.NEWS_DZEN)

    @allure.step("Переключиться на последнюю открытую вкладку")
    def go_to_last_tab(self):
        self._switch_to_last_tab()

    @allure.step("Проверить, что окно успешного оформления заказа отображается")
    def is_order_completed_displayed(self):
        try:
            self._is_visible(OrderPageLocators.ORDER_COMPLETED)
            return True
        except:
            return False

    @allure.step("Проверить, что произошел успешный переход на главную страницу Самоката")
    def is_home_header_displayed(self):
        try:
            self._is_visible(MainPageLocators.HOME_HEADER)
            return True
        except:
            return False

    @allure.step("Проверить, что окно успешного оформления заказа отображается")
    def is_news_dzen_displayed(self):
        try:
            self._is_visible(OrderPageLocators.NEWS_DZEN)
            return True
        except:
            return False

    @allure.step("Сценарий заказа 1 - Заполнение данных 'Для кого самокат'")
    #def order_script_1_step_1(self, name, surname, address, phone_number):
    def filling_data_who_scooter_for_script_1(self, name, surname, address, phone_number):
        self.click_order_button_main_page()
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro()
        self.enter_phone_number(phone_number)
        self.click_next_button()
        return self

    @allure.step("Сценарий заказа 1 - Заполнение данных 'Про аренду'")
    def filling_data_for_rent_script_1(self, date):
        self.enter_order_date(date)
        self.enter_rental_period_one_day()
        self.click_color_black_checkbox()
        self.click_order_button_order_page()
        self.click_confirm_button()
        return self

    @allure.step("Переход на главную страницу через логотип Самоката")
    def access_to_main_page_via_samokat_logo(self):
        self.click_view_status_button()
        self.click_logo_scooter()
        return self

    @allure.step("Сценарий заказа 2 - Заполнение данных 'Для кого самокат'")
    def filling_data_who_scooter_for_script_2(self, name, surname, address, phone_number):
        self.scroll_to_order_big_button()
        self.click_order_big_button_main_page()
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro()
        self.enter_phone_number(phone_number)
        self.click_next_button()
        return self

    @allure.step("Сценарий заказа 2 - Заполнение данных 'Про аренду'")
    def filling_data_for_rent_script_2(self, date):
        self.enter_order_date(date)
        self.enter_rental_period_two_day()
        self.click_color_grey_checkbox()
        self.click_order_button_order_page()
        self.click_confirm_button()
        return self

    @allure.step("Переход на страницу Дзена через логотип Яндекса")
    def access_to_dzen_page_via_yandex_logo(self):
        self.click_logo_yandex()
        self.go_to_last_tab()
        return self
