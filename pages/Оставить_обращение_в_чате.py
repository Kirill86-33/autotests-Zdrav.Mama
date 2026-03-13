from pages.base_page import BasePage

class CardChatRequest(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    BUTTON_JUMP = ("xpath", "(//div//button)[54]")
    CARD_CHAT_REQUEST = ("xpath", "(//div//a)[24]")
 
  

    def click_button_jump (self):  
        button_jump = self.driver.find_element(*self.BUTTON_JUMP) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_jump)


    def click_card_chat_request (self):  
        card_chat_request = self.driver.find_element(*self.CARD_CHAT_REQUEST) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", card_chat_request)