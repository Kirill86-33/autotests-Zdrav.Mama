from testit_python_commons.decorators import externalId, displayName

class TestLeaveForm:
    @externalId("test_leave_form")
    @displayName("Форма 'Родить в Подмосковье'")
    def test_leave_form(self, leave_page):
        """Тест формы 'Родить в Подмосковье'"""
        leave_page.open()
        leave_page.click_send_leave()
        leave_page.enter_name("ТЕСТ ТЕСТ")
        leave_page.enter_phone("+73333333333")
        leave_page.enter_email("test@yandex.ru")
        leave_page.enter_district("Московская область")  
        leave_page.click_send_button()
        
        print("✓ Форма успешно заполнена и отправлена")