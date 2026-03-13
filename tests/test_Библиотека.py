import pytest

class TestLibraryPage:
    def test_card_library(self, card_library ):
        card_library.open()
        card_library.click_button_jump()
        card_library.click_button_jump()
        card_library.click_button_jump()
        card_library.click_card_library()