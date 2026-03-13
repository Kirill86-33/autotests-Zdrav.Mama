import pytest

class TestLinkCityPage:
    def test_link_city(self, input_search_city ):  # Фикстура автоматически передаст login_page
        input_search_city.open()
        input_search_city.click_button_list()
        input_search_city.enter_input_city("Балашиха")
        input_search_city.click_button_city()
        input_search_city.click_map_lpu()