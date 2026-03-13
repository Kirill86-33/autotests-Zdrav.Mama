import pytest

class TestDoctorsForm:
    def test_all_doctors(self, button_doctors):
        button_doctors.open()
        button_doctors.click_button_doctors()