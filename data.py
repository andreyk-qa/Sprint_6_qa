from locators.main_page_locators import MainPageLocators


class QuestionsAndAnswers:

    QUESTIONS_AND_ANSWERS = [
        (
            MainPageLocators.DROP_LIST_QUESTIONS_1_HEADING,
            MainPageLocators.DROP_LIST_QUESTIONS_1_PANEL,
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        ),
        (
            MainPageLocators.DROP_LIST_QUESTIONS_2_HEADING,
            MainPageLocators.DROP_LIST_QUESTIONS_2_PANEL,
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        ),
        (
            MainPageLocators.DROP_LIST_QUESTIONS_3_HEADING,
            MainPageLocators.DROP_LIST_QUESTIONS_3_PANEL,
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        ),
        (
            MainPageLocators.DROP_LIST_QUESTIONS_4_HEADING,
            MainPageLocators.DROP_LIST_QUESTIONS_4_PANEL,
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        ),
        (
            MainPageLocators.DROP_LIST_QUESTIONS_5_HEADING,
            MainPageLocators.DROP_LIST_QUESTIONS_5_PANEL,
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        ),
        (
            MainPageLocators.DROP_LIST_QUESTIONS_6_HEADING,
            MainPageLocators.DROP_LIST_QUESTIONS_6_PANEL,
            'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        ),
        (
            MainPageLocators.DROP_LIST_QUESTIONS_7_HEADING,
            MainPageLocators.DROP_LIST_QUESTIONS_7_PANEL,
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        ),
        (
            MainPageLocators.DROP_LIST_QUESTIONS_8_HEADING,
            MainPageLocators.DROP_LIST_QUESTIONS_8_PANEL,
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        ),
    ]

class Url:

    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
