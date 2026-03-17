from testit_python_commons.decorators import externalId, displayName

class TestServicesForm:
    @externalId("test_services_form")
    @displayName("Кнопка 'Услуги'")
    def test_services_form(self, button_services):
        button_services.open()
        button_services.click_button_services()