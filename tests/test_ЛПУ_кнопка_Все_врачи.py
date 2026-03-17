from testit_python_commons.decorators import externalId, displayName

class TestDoctorsForm:
    @externalId("test_all_doctors")
    @displayName("Кнопка 'Все врачи'")
    def test_all_doctors(self, button_doctors):
        button_doctors.open()
        button_doctors.click_button_doctors()