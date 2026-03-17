from testit_python_commons.decorators import externalId, displayName

class TestCallMePage:
    @externalId("test_button_call_me")
    @displayName("Кнопка 'Позвоните мне'")
    def test_button_call_me(self, button_call_me):  
        button_call_me.open()
        button_call_me.enter_phone("+73333333333")
        button_call_me.click_button_call_me()