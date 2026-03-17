from testit_python_commons.decorators import externalId, displayName

class TestFormRight:
    @externalId("test_right_form")
    @displayName("Кнопка 'Вправо'")
    def test_right_form(self, button_right ):
        button_right.open()
        button_right.click_button_right_arrow()