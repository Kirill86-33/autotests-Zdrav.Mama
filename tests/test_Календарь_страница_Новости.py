from testit_python_commons.decorators import externalId, displayName

class TestCalendarForm:
    @externalId("test_button_calendar")
    @displayName("Кнопка 'Календарь'")
    def test_button_calendar(self, button_calendar):
        button_calendar.open()
        button_calendar.click_button_information()