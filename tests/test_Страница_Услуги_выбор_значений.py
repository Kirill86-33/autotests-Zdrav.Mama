from testit_python_commons.decorators import externalId, displayName

class TestArticlesForm:
    @externalId("test_articles_servuces")
    @displayName("Статьи и услуги")
    def test_articles_servuces(self, button_articles_services):
        button_articles_services.open()
        button_articles_services.click_button_articles_services()