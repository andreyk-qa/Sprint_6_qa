import pytest
from data import QuestionsAndAnswers
from pages.main_page import MainPage


class TestDropListQuestions:

    @pytest.fixture
    def main_page(self, driver):
        return MainPage(driver)

    @pytest.mark.parametrize('heading_locator, panel_locator, expected_answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS)
    def test_drop_list_questions(self, main_page, heading_locator, panel_locator, expected_answer):
        main_page.open()
        main_page.click_question_heading(heading_locator)
        actual_answer = main_page.get_answer_text(panel_locator)
        assert expected_answer == actual_answer
