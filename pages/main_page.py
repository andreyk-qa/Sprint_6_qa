from .base_page import BasePage
from data import Url


class MainPage(BasePage):

    def open(self):
        self.driver.get(Url.MAIN_PAGE_URL)
        return self

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_question_heading(self, heading_locator):
        self.scroll_to_element(heading_locator)
        element = self.wait.until(self.EC.element_to_be_clickable(heading_locator))
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, panel_locator):
        panel_element = self.wait.until(self.EC.visibility_of_element_located(panel_locator))
        return panel_element.text
