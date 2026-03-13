import pytest

class TestServicesForm:
    def test_services_form(self, button_services):
        button_services.open()
        button_services.click_button_services()