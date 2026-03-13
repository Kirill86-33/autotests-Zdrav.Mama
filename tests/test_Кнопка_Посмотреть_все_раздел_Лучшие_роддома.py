import pytest

class TestViewForm:
    def test_view_form(self, button_view_all):
        button_view_all.open()
        button_view_all.click_button_view()