from testit_python_commons.decorators import externalId, displayName

class TestViewForm:
    @externalId("test_view_form")
    @displayName("Кнопка 'Смотреть все'")
    def test_view_form(self, button_view_all):
        button_view_all.open()
        button_view_all.click_button_view()