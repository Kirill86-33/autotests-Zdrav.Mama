from testit_python_commons.decorators import externalId, displayName

class TestShowAllForm:
    @externalId("test_show_form")
    @displayName("Кнопка 'Показать все'")
    def test_show_form(self, button_show_all ):
        button_show_all.open()
        button_show_all.click_button_show_all()