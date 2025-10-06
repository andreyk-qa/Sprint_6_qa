import pytest
import allure
from data import OrderTestData


class TestOrders:

    @allure.title("Проверка успешного оформления заказа")
    @allure.description("Проверяется позитивный сценарий оформления заказа через верхнюю или нижнюю кнопку и наличие всплывающего окна 'Заказ оформлен'.")
    @pytest.mark.parametrize('test_data', OrderTestData.ORDER_TEST_DATA)
    def test_successful_order(self, order_page, test_data):
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
        assert order_page.is_order_completed_displayed()
