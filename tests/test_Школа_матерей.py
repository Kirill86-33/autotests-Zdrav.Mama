from testit_python_commons.decorators import externalId, displayName

class TestCardMothersSchool:
    @externalId("test_card_mothers_school")
    @displayName("Карточка школы матерей")
    def test_card_mothers_school(self, card_mothers_school):
        card_mothers_school.open()
        card_mothers_school.click_card_mothers_school()