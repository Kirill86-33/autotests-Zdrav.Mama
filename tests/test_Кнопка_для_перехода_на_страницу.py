from testit_python_commons.decorators import externalId, displayName

class TestNumberKeyForm:
    @externalId("test_button_number_key")
    @displayName("Кнопка 'Новости' (цифровая клавиша)")
    def test_button_number_key(self, button_news_key):
        button_news_key.open()
        button_news_key.click_button_number_keys()