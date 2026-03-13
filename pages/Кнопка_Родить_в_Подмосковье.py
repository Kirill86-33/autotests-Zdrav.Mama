from pages.base_page import BasePage

class BirthPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/header_birth'


    INPUT_NAME = ("xpath", "//input[@id ='name']")
    INPUT_PHONE = ("xpath", "//input[@id ='phone']")
    INPUT_EMAIL = ("xpath", "//input[@id ='email']")
    INPUT_DISTRICT = ("xpath", "//input[@id ='district']")
    BUTTON_SEND = ("xpath", "//button[text()='Отправить']")

    
    def enter_name (self, name):  
        input_name = self.driver.find_element(*self. INPUT_NAME )
        input_name.send_keys(name)

    def enter_phone (self, phone):  
        input_phone = self.driver.find_element(*self. INPUT_PHONE )
        input_phone.send_keys(phone)

    def enter_email (self, email):  
        input_email = self.driver.find_element(*self. INPUT_EMAIL )
        input_email.send_keys(email)

    def enter_district (self, district):  
        input_district  = self.driver.find_element(*self. INPUT_DISTRICT )
        input_district .send_keys(district)


    def click_send_button(self):
        button = self.driver.find_element(*self.BUTTON_SEND)
        self.driver.execute_script("arguments[0].click();", button)