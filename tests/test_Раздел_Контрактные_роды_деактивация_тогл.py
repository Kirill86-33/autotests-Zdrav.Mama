import pytest

class TestToglPage:
    
    def test_select_togl(self, button_togl):  
        button_togl.open()
        button_togl.click_togl()
        button_togl.click_button_offer()
        button_togl.enter_name("ТЕСТ ТЕСТ")
        button_togl.enter_phone("+73333333333")
        button_togl.enter_email("test@yandex.ru")
        button_togl.enter_district("Московская область")  
        button_togl.click_send_button()



        
       