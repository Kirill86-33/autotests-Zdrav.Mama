

class TestBirthForm:
    def test_birth_form(self, birth_page):
        birth_page.open()
        birth_page.enter_name("ТЕСТ ТЕСТ")
        birth_page.enter_phone("+73333333333")
        birth_page.enter_email("test@yandex.ru")
        birth_page.enter_district("Московская область")  
        
        birth_page.click_send_button()
        
        print("✓ Форма успешно заполнена и отправлена")