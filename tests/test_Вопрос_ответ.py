import pytest

class TestCardQuestion:
    def test_card_question_answer(self, card_question_answer ):
        card_question_answer.open()
        card_question_answer.click_button_jump()
        card_question_answer.click_card_question_answer()