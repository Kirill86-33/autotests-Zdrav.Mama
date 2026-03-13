from pages.base_page import BasePage

class BlockSpecialization(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/clinics'

    BLOCK_SPECIALIZATION = ("xpath", "(//div//span[text()='Беременности с ЭКО'])[1]")
 
  
    def enter_meaning_block_specialization (self):  
        meaning_specialization = self.driver.find_element(*self.BLOCK_SPECIALIZATION) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", meaning_specialization)


    