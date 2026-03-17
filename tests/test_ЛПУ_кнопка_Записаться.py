from testit_python_commons.decorators import externalId, displayName

class TestRegisterForm:
    @externalId("test_register_form")
    @displayName("Форма регистрации")
    def test_register_form(self, register_page):# register_page - это название созданной фикстуры и используется в тесте
        """Тест формы 'Родить в Подмосковье'"""
        register_page.open()
        register_page.click_button_register()
        register_page.enter_name("ТЕСТ ТЕСТ")
        register_page.enter_phone("+73333333333")
        register_page.enter_email("test@yandex.ru")
        register_page.enter_district("Московская область")  
        register_page.click_send_button()
        
        print("✓ Форма успешно заполнена и отправлена")