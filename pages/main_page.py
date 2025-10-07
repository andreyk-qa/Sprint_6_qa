from .base_page import BasePage
from data import Url
import allure


class MainPage(BasePage):

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self._open_url(Url.MAIN_PAGE_URL)

    @allure.step("Кликнуть по заголовку вопроса")
    def click_question_heading(self, heading_locator):
        self._scroll_to_element(heading_locator)
        element = self.wait.until(self.EC.element_to_be_clickable(heading_locator))
        self._execute_script("arguments[0].click();", element)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, panel_locator):
        return self._get_text(panel_locator)
