import pytest

class TestCardGynecologist:
    def test_card_gynecologist(self, card_gynecologist):
        card_gynecologist.open()
        card_gynecologist.click_card_gynecologist()