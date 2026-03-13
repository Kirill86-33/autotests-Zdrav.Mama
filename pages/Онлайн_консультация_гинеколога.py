from pages.base_page import BasePage

class CardGynecologist(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    CARD_ONLINE_GYNECOLOGIST = ("xpath", "(//div//a)[19]")
 
  

    def click_card_gynecologist (self):  
        card_gynecologist = self.driver.find_element(*self.CARD_ONLINE_GYNECOLOGIST) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", card_gynecologist)