from pages.base_page import BasePage

class CardFirstPregnancy(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    BUTTON_JUMP = ("xpath", "(//div//button)[54]")
    CARD_FIRST_PREGNANCY = ("xpath", "(//div//a)[23]")
 
  

    def click_button_jump (self):  
        button_jump = self.driver.find_element(*self.BUTTON_JUMP) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_jump)


    def click_card_first_pregnancy (self):  
        card_pregnancy = self.driver.find_element(*self.CARD_FIRST_PREGNANCY) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", card_pregnancy)