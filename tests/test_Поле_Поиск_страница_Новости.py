import pytest

class TestLinkNewsPage:
    
    def test_link_news(self, input_search_news ):  # Фикстура автоматически передаст login_page
        input_search_news.open()
        input_search_news.click_enter_input_news("Вакцинация")
       

        