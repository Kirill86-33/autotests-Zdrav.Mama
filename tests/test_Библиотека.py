from testit_python_commons.decorators import externalId, displayName

class TestLibraryPage:
    @externalId("test_card_library")
    @displayName("Карточка библиотеки")
    def test_card_library(self, card_library ):
        card_library.open()
        card_library.click_button_jump()
        card_library.click_button_jump()
        card_library.click_button_jump()
        card_library.click_card_library()