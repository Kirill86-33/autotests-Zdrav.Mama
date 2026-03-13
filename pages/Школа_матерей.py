from pages.base_page import BasePage

class CardMothersSchool(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    CARD_MOTHERS_SCHOOL = ("xpath", "(//div//a)[21]")
 
  

    def click_card_mothers_school (self):  
        card_mothers = self.driver.find_element(*self.CARD_MOTHERS_SCHOOL) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", card_mothers)