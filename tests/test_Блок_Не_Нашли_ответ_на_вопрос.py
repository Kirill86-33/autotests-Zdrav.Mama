import pytest

class TestNotFoundAnswerForm:
    def test_not_found_answer_form(self, input_not_found_answer):
        input_not_found_answer.open()
        input_not_found_answer.enter_name("ТЕСТ ТЕСТ")
        input_not_found_answer.enter_phone("+73333333333")
        input_not_found_answer.enter_email("test@yandex.ru")
        input_not_found_answer.enter_district("Московская область")  
        input_not_found_answer.enter_comment("НЕ ЗВОНИТЬ! ТЕСТОВЫЙ КОММЕНТАРИЙ") 
        input_not_found_answer.click_send_button()
        
   