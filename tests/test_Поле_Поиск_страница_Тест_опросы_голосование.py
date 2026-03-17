from testit_python_commons.decorators import externalId, displayName

class TestSearchVoting:
    @externalId("test_search_test_voting")
    @displayName("Поиск теста голосования")
    def test_search_test_voting(self, search_test_voting ):  # Фикстура автоматически передаст login_page
        search_test_voting.open()
        search_test_voting.click_search_enter_test("Роды")