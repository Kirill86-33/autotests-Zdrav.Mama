from testit_python_commons.decorators import externalId, displayName

class TestCardMaternityHospital:
    @externalId("test_card_maternity")
    @displayName("Карточка роддома")
    def test_card_maternity(self, card_maternity_hospital):
        card_maternity_hospital.open()
        card_maternity_hospital.click_button_jump()
        card_maternity_hospital.click_card_maternity_hospital()