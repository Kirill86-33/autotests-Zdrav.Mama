import pytest

class TestPassingPage:
    
    def test_passing(self, test_passing_mothers_school):  
        test_passing_mothers_school.open()
        test_passing_mothers_school.click_button_before_birth()
        test_passing_mothers_school.click_button_answer_1()
        test_passing_mothers_school.click_button_next_1 
        test_passing_mothers_school.click_button_answer_2
        test_passing_mothers_school.click_button_next_2
        test_passing_mothers_school.click_button_answer_3
        test_passing_mothers_school.click_button_next_3
        test_passing_mothers_school.click_button_answer_4
        test_passing_mothers_school.click_button_result