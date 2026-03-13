import pytest

class TestSideKeys:
    
    def test_button_online_service(self,  online_service):  
        online_service.open()
        online_service.click_button_right()
        online_service.click_button_left()
       