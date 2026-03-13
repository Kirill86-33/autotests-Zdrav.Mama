from pages.base_page import BasePage

class CardSurveys(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/news'

    CARD_TEST_VOTING = ("xpath", "(//div//a)[20]")
 
  

    def click_card_voting (self):  
        card_voting = self.driver.find_element(*self.CARD_TEST_VOTING) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", card_voting)