import pytest

class TestArticlesForm:
    def test_articles_servuces(self, button_articles_services):
        button_articles_services.open()
        button_articles_services.click_button_articles_services()