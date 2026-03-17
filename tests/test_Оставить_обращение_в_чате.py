from testit_python_commons.decorators import externalId, displayName

class TestCardChatRequest:
    @externalId("test_card_chat")
    @displayName("Карточка чата")
    def test_card_chat(self, card_chat_request ):
        card_chat_request.open()
        card_chat_request.click_button_jump()
        card_chat_request.click_button_jump()#Два раза нажатие на боковую клавишу
        card_chat_request.click_card_chat_request()