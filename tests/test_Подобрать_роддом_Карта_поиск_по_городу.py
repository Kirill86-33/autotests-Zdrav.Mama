import pytest

class TestMapCityPage:
    def test_map_city(self, button_search_city ):  # Фикстура автоматически передаст login_page
        button_search_city.open()
        button_search_city.click_button_map()
        button_search_city.enter_input_city("Балашиха")
        button_search_city.click_button_city()
        