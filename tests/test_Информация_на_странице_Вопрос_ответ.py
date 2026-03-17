from testit_python_commons.decorators import externalId, displayName

class TestInformationForm:
    @externalId("test_button_information")
    @displayName("Кнопка 'Информация'")
    def test_button_information(self, input_page_question_answer):
        input_page_question_answer.open()
        input_page_question_answer.click_button_information()