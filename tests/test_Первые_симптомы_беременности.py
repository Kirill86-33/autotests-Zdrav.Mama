from testit_python_commons.decorators import externalId, displayName

class TestCardFirstPregnancy:
    @externalId("test_card_pregnancy")
    @displayName("Карточка 'Первая беременность'")
    def test_card_pregnancy(self, card_first_pregnancy):
        card_first_pregnancy.open()
        card_first_pregnancy.click_button_jump()
        card_first_pregnancy.click_card_first_pregnancy()