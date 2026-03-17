from testit_python_commons.decorators import externalId, displayName

class TestButtonAllNews:
    @externalId("test_all_news")
    @displayName("Кнопка 'Все новости'")
    def test_all_news(self, button_all_news):
        button_all_news.open()
        button_all_news.click_button_all_news()