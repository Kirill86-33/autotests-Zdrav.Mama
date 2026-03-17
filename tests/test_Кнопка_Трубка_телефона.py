from testit_python_commons.decorators import externalId, displayName

class TestPhoneForm:
    @externalId("test_phone_form")
    @displayName("Кнопка телефона")
    def test_phone_form(self, button_phone):
        button_phone.open()
        button_phone.click_button_phone()
       