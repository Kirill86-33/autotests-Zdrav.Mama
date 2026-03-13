import pytest

class TestShowAllForm:
    def test_show_form(self, button_show_all ):
        button_show_all.open()
        button_show_all.click_button_show_all()