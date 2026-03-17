from testit_python_commons.decorators import externalId, displayName

class TestCardVoting:
    @externalId("test_card_voting")
    @displayName("Карточка голосования")
    def test_card_voting(self, card_test_voting):
        card_test_voting.open()
        card_test_voting.click_card_voting()