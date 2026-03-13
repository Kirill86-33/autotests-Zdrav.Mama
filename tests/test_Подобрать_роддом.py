import pytest

class TestCardMaternityHospital:
    def test_card_maternity(self, card_maternity_hospital):
        card_maternity_hospital.open()
        card_maternity_hospital.click_button_jump()
        card_maternity_hospital.click_card_maternity_hospital()