import pytest

class TestCardVoting:
    def test_card_voting(self, card_test_voting):
        card_test_voting.open()
        card_test_voting.click_card_voting()