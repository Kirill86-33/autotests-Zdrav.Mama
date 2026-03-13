import pytest

class TestCardFirstPregnancy:
    def test_card_pregnancy(self, card_first_pregnancy):
        card_first_pregnancy.open()
        card_first_pregnancy.click_button_jump()
        card_first_pregnancy.click_card_first_pregnancy()