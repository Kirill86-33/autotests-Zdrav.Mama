import pytest

class TestCalendarForm:
    def test_button_calendar(self, button_calendar):
        button_calendar.open()
        button_calendar.click_button_information()