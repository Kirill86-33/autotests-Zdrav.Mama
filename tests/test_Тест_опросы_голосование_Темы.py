import pytest

class TestSelectingForm:
    def test_button_selecting(self, button_selecting_topic):
        button_selecting_topic.open()
        button_selecting_topic.click_button_topic()