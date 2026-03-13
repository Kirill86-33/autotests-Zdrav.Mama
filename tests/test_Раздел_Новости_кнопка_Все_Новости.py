import pytest

class TestButtonAllNews:
    def test_all_news(self, button_all_news):
        button_all_news.open()
        button_all_news.click_button_all_news()