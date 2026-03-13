import pytest

class TestFindForm:
    def test_find_form(self, button_find):
        button_find.open()
        button_find.click_button_find()

