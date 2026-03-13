import pytest

class TestInformationForm:
    def test_button_information(self, input_page_question_answer):
        input_page_question_answer.open()
        input_page_question_answer.click_button_information()