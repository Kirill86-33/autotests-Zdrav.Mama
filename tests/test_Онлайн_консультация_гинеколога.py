from testit_python_commons.decorators import externalId, displayName

class TestCardGynecologist:
    @externalId("test_card_gynecologist")
    @displayName("Карточка гинеколога")
    def test_card_gynecologist(self, card_gynecologist):
        card_gynecologist.open()
        card_gynecologist.click_card_gynecologist()