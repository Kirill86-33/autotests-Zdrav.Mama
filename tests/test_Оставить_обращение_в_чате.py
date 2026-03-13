import pytest

class TestCardChatRequest:
    def test_card_chat(self, card_chat_request ):
        card_chat_request.open()
        card_chat_request.click_button_jump()
        card_chat_request.click_button_jump()#Два раза нажатие на боковую клавишу
        card_chat_request.click_card_chat_request()