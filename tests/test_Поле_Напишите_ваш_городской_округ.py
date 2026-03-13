import pytest


class TestLinkYourCounty:
    def test_link_your_county(self, input_field_your_county ):  # Фикстура автоматически передаст login_page
        input_field_your_county.open()
        input_field_your_county.click_input_your_county
        input_field_your_county.enter_input_your_county("Балашиха")
        input_field_your_county.click_button_city ()
        