import pytest
from pages.order_page import OrderPage
import allure


class TestOrders:

    @pytest.fixture
    def order_page(self, driver):
        return OrderPage(driver)

    @allure.title("Проверка успешного оформления заказа через верхнюю кнопку")
    @allure.description("Проверяется позитивный сценарий оформления заказа через кнопку 'Заказать' вверху страницы и наличие всплывающего окна 'Заказ оформлен'.")
    def test_order_page_script_1(self, order_page):
        order_page.open()
        order_page.order_script_1_step_1("Григорий", "Кукумбер", "За тридевять земель", "+7999999999")
        order_page.order_script_1_step_2("01.01.2030")
        text = order_page.get_text_completed_order()
        assert 'Заказ оформлен' in text

    @allure.title("Проверка перехода на Главную страницу Самоката")
    @allure.description("Проверяется, что при клике на логотип 'Самокат' происходит переход на главную страницу.")
    def test_transition_to_main_page_via_logo_scooter(self, order_page):
        order_page.open()
        order_page.order_script_1_step_1("Григорий", "Кукумбер", "За тридевять земель", "+7999999999")
        order_page.order_script_1_step_2("01.01.2030")
        order_page.order_script_1_step_3()
        text = order_page.get_text_home_header()
        assert 'Самокат' in text

    @allure.title("Проверка успешного оформления заказа через нижнюю кнопку")
    @allure.description("Проверяется позитивный сценарий оформления заказа через кнопку 'Заказать' внизу страницы и наличие всплывающего окна 'Заказ оформлен'.")
    def test_order_page_script_2(self, order_page):
        order_page.open()
        order_page.order_script_2_step_1("Афанасий", "Известный", "Далеко", "+7888888888")
        order_page.order_script_2_step_2("08.15.2026")
        text = order_page.get_text_completed_order()
        assert 'Заказ оформлен' in text

    @allure.title("Проверка перехода на страницу Дзена")
    @allure.description("Проверяется, что при клике на логотип 'Яндекс' в новом окне открывается главная страница Дзена.")
    def test_transition_to_dzen_page_via_logo_yandex(self, order_page):
        order_page.open()
        order_page.order_script_2_step_1("Афанасий", "Известный", "Далеко", "+7888888888")
        order_page.order_script_2_step_2("08.15.2026")
        order_page.order_script_2_step_3()
        text = order_page.get_text_news_dzen()
        assert 'Новости' in text
