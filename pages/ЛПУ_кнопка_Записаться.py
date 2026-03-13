from pages.base_page import BasePage

class RegisterHospitalPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/top_clinics/gbuz-mo-moskovskij-oblastnoj-nauchno-issledovatelskij-institut-akusherstv-i-ginekologii'

    BUTTON_REGISTER = ("xpath", "//*[@id='__next']/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[5]/div")
    INPUT_NAME = ("xpath", "//input[@id ='name']")
    INPUT_PHONE = ("xpath", "//input[@id ='phone']")
    INPUT_EMAIL = ("xpath", "//input[@id ='email']")
    INPUT_DISTRICT = ("xpath", "//input[@id ='district']")
    BUTTON_SEND = ("xpath", "//button[text()='Отправить']")

    

    def click_button_register(self):
        button_register = self.driver.find_element(*self.BUTTON_REGISTER)
        self.driver.execute_script("arguments[0].click();", button_register)

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