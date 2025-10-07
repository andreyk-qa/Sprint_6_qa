from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.EC = EC

    @allure.step("Открыть URL: {url}")
    def _open_url(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент по локатору: {locator}")
    def _find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть по элементу: {locator}")
    def _click(self, locator):
        self.wait.until(self.EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def _send_keys(self, locator, text):
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def _get_text(self, locator):
        return self.wait.until(self.EC.visibility_of_element_located(locator)).text

    @allure.step("Проверить, что элемент {locator} отображается")
    def _is_visible(self, locator):
            self.wait.until(self.EC.visibility_of_element_located(locator))

    @allure.step("Прокрутить страницу до элемента: {locator}")
    def _scroll_to_element(self, locator):
        element = self.wait.until(self.EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Выполнить JavaScript: {script}")
    def _execute_script(self, script, element=None):
        if element:
            self.driver.execute_script(script, element)
        else:
            self.driver.execute_script(script)

    @allure.step("Переключиться на последнюю открытую вкладку")
    def _switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
