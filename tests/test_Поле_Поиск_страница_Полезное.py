from testit_python_commons.decorators import externalId, displayName


class TestLinkUsefulPage:
    @externalId("test_link_useful")
    @displayName("Поиск полезной информации")
    def test_link_useful(self, input_search_useful ):  # Фикстура автоматически передаст login_page
        input_search_useful.open()
        input_search_useful.click_enter_input_useful("Вакцинация")
        input_search_useful.click_information()
    