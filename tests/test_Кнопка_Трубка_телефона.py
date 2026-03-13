import pytest

class TestPhoneForm:
    def test_phone_form(self, button_phone):
        button_phone.open()
        button_phone.click_button_phone()
       