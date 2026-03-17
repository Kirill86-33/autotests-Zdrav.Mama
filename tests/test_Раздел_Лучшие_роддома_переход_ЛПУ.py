from testit_python_commons.decorators import externalId, displayName

class TestHospitalForm:
    @externalId("test_hospital_form")
    @displayName("Кнопка 'Больница'")  
    def test_hospital_form(self, button_hospital):
        button_hospital.open()
        button_hospital.click_button_hospital()