from pages.base_page import BasePage

class CardLibrary(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    BUTTON_JUMP = ("xpath", "(//div//button)[54]")
    CARD_LIBRARY = ("xpath", "(//div//a)[26]")
 
  

    def click_button_jump (self):  
        button_jump = self.driver.find_element(*self.BUTTON_JUMP) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_jump)


    def click_card_library (self):  
        card_library = self.driver.find_element(*self.CARD_LIBRARY) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", card_library)