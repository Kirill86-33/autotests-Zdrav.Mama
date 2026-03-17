from testit_python_commons.decorators import externalId, displayName

class TestUniquePage:
    @externalId("test_button_unique_offer")
    @displayName("Уникальное предложение")
    def test_button_unique_offer(self, button_unique_offer ):  
        button_unique_offer.open()
        button_unique_offer.click_unique_offer()
        button_unique_offer.enter_name("ТЕСТ ТЕСТ")
        button_unique_offer.enter_phone("+73333333333")
        button_unique_offer.enter_email("test@yandex.ru")
        button_unique_offer.enter_district("Московская область")  
        button_unique_offer.click_send_button()