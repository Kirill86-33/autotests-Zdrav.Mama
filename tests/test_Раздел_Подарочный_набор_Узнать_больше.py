from testit_python_commons.decorators import externalId, displayName

class TestFindForm:
    @externalId("test_find_form")
    @displayName("Кнопка 'Найти'")
    def test_find_form(self, button_find):
        button_find.open()
        button_find.click_button_find()

