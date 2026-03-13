import pytest

class TestSearchVoting:
    
    def test_search_test_voting(self, search_test_voting ):  # Фикстура автоматически передаст login_page
        search_test_voting.open()
        search_test_voting.click_search_enter_test("Роды")