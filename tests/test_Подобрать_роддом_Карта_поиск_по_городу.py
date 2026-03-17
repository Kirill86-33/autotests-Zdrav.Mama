from testit_python_commons.decorators import externalId, displayName

class TestMapCityPage:
    @externalId("test_map_city")
    @displayName("Поиск города на карте")
    def test_map_city(self, button_search_city ):  # Фикстура автоматически передаст login_page
        button_search_city.open()
        button_search_city.click_button_map()
        button_search_city.enter_input_city("Балашиха")
        button_search_city.click_button_city()
        