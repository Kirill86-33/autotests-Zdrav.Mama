from testit_python_commons.decorators import externalId, displayName

class TestSideKeys:
    @externalId("test_button_online_service")
    @displayName("Кнопки онлайн-сервиса (вправо/влево)")
    def test_button_online_service(self,  online_service):  
        online_service.open()
        online_service.click_button_right()
        online_service.click_button_left()
       