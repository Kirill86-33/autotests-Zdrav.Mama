from pages.base_page import BasePage

class SearchClinic(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/clinics'

    INPUT_CLINIC = ("xpath", "//*[@id=':r1:']")
    
  
    def click_enter_input_clinic (self, driver):  
        input_clinic = self.driver.find_element(*self.INPUT_CLINIC) # Добавляем явное ожидание
        input_clinic.send_keys(driver)
