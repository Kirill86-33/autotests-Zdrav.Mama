from testit_python_commons.decorators import externalId, displayName

class TestPassingPage:
    @externalId("test_passing")
    @displayName("Прохождение теста (первый вариант)")
    def test_passing(self, button_passing_test ):  
        button_passing_test.open()
        button_passing_test.click_button_passing_test()
        button_passing_test.click_button_answer_1()
        button_passing_test.click_button_next_1()
        button_passing_test.click_button_answer_2()
        button_passing_test.click_button_next_2()
        button_passing_test.click_button_answer_3()
        button_passing_test.click_button_next_3()
        button_passing_test.click_button_answer_4()
        button_passing_test.click_button_result()