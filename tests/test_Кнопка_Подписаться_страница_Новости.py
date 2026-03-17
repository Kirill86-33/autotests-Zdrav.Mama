from testit_python_commons.decorators import externalId, displayName
class TestSubscribeForm:
    @externalId("test_button_subscribe")
    @displayName("Подписка на новости")
    def test_button_Subscribe(self, button_subscribe):
        button_subscribe.open()
        button_subscribe.click_button_subscribe()
        button_subscribe.enter_email("test@yandex.ru")
        button_subscribe.click_button_subscribe_2()
        
       