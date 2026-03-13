from pages.base_page import BasePage

class ButtonCallMePage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    INPUT_PHONE = ("xpath", "//input[@id ='phone']")
    BUTTON_CALL_ME = ("xpath", "//div//button[@type='submit']")
   
   
    def enter_phone (self, phone):  
        input_phone = self.driver.find_element(*self. INPUT_PHONE )
        input_phone.send_keys(phone)


    def click_button_call_me(self):
        button_call = self.driver.find_element(*self.BUTTON_CALL_ME)
        self.driver.execute_script("arguments[0].click();", button_call)