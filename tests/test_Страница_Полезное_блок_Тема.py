from testit_python_commons.decorators import externalId, displayName
class TestTopicForm:
    @externalId("test_button_topic")
    @displayName("Кнопка 'Тема'")
    def test_button_topic(self, button_topic):
        button_topic.open()
        button_topic.click_button_topic()