from testit_python_commons.decorators import externalId, displayName

class TestCardQuestion:
    @externalId("test_card_question_answer")
    @displayName("Карточка вопроса-ответа")
    def test_card_question_answer(self, card_question_answer ):
        card_question_answer.open()
        card_question_answer.click_button_jump()
        card_question_answer.click_card_question_answer()