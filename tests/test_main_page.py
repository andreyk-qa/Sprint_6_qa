import pytest
from data import QuestionsAndAnswers, OrderTestData
import allure


class TestDropListQuestions:

    @allure.title("Проверка выпадающего списка 'Вопросы о важном'")
    @allure.description("Проверка, что при клике на каждый из 8 вопросов выпадающего списка отображается соответствующий корректный ответ.")
    @pytest.mark.parametrize('heading_locator, panel_locator, expected_answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS)
    def test_drop_list_questions(self, main_page, heading_locator, panel_locator, expected_answer):
        main_page.open()
        main_page.click_question_heading(heading_locator)
        actual_answer = main_page.get_answer_text(panel_locator)
        assert expected_answer == actual_answer

    @allure.title("Проверка перехода на главную страницу Самоката")
    @allure.description("Проверяется, что при клике на логотип 'Самокат' происходит переход на главную страницу.")
    @pytest.mark.parametrize('test_data', [OrderTestData.ORDER_SCRIPT_1])
    def test_transition_to_main_page_via_logo_scooter(self, order_page, test_data):
        order_page.open()
        filling_data_who_scooter = getattr(order_page, test_data['filling_data_function'])
        filling_data_who_scooter(
            test_data['name'],
            test_data['surname'],
            test_data['address'],
            test_data['phone_number']
        )
        filling_data_for_rent = getattr(order_page, test_data['filling_rent_function'])
        filling_data_for_rent(test_data['date'])
        order_page.access_to_main_page_via_samokat_logo()
        assert order_page.is_home_header_displayed()

    @allure.title("Проверка перехода на страницу Дзена")
    @allure.description("Проверяется, что при клике на логотип 'Яндекс' в новом окне открывается главная страница Дзена.")
    def test_transition_to_dzen_page_via_logo_yandex(self, order_page):
        order_page.open()
        order_page.access_to_dzen_page_via_yandex_logo()
        assert order_page.is_news_dzen_displayed()