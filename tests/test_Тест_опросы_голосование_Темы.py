from testit_python_commons.decorators import externalId, displayName

class TestSelectingForm:
    @externalId("test_button_selecting")
    @displayName("Выбор темы")
    def test_button_selecting(self, button_selecting_topic):
        button_selecting_topic.open()
        button_selecting_topic.click_button_topic()