import pytest

class TestHospitalForm:
    def test_hospital_form(self, button_hospital):
        button_hospital.open()
        button_hospital.click_button_hospital()