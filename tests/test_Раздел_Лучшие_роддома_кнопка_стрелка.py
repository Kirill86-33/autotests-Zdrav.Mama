import pytest

class TestFormRight:
    def test_right_form(self, button_right ):
        button_right.open()
        button_right.click_button_right_arrow()