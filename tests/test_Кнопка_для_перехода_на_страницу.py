import pytest

class TestNumberKeyForm:
    def test_button_number_key(self, button_news_key):
        button_news_key.open()
        button_news_key.click_button_number_keys()