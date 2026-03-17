from testit_python_commons.decorators import externalId, displayName

class TestTagNewsPage:
    @externalId("test_tag_news")
    @displayName("Тег новости")
    def test_tag_news(self,  button_tag_news ):  # select_tab - это название созданной фикстура
         button_tag_news.open()
         button_tag_news.click_button_tag()