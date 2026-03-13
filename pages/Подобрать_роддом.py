from pages.base_page import BasePage

class CardMaternityHospital(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    BUTTON_JUMP = ("xpath", "(//div//button)[54]")
    CARD_MATERNITY_HOSPITAL = ("xpath", "(//div//a)[22]")
 
  

    def click_button_jump (self):  
        button_jump = self.driver.find_element(*self.BUTTON_JUMP) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_jump)


    def click_card_maternity_hospital (self):  
        card_maternity = self.driver.find_element(*self.CARD_MATERNITY_HOSPITAL) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", card_maternity)