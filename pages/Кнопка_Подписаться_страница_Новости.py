from pages.base_page import BasePage

class ButtonSubscribePage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/news'

    BUTTON_SUBSCRIBE = ("xpath", "//div//button[text()='Подписаться']")
    INPUT_EMAIL = ("xpath", "//input[@id ='email']")
    BUTTON_SUBSCRIBE_2 = ("xpath", "(//div//button[text()='Подписаться'])[2]")



    def click_button_subscribe(self):
        button_subscribe = self.driver.find_element(*self.BUTTON_SUBSCRIBE)
        self.driver.execute_script("arguments[0].click();", button_subscribe)   
    

    def enter_email (self, email):  
        input_email = self.driver.find_element(*self. INPUT_EMAIL )
        input_email.send_keys(email)


    def click_button_subscribe_2(self):
        button_subscribe_2 = self.driver.find_element(*self.BUTTON_SUBSCRIBE_2)
        self.driver.execute_script("arguments[0].click();", button_subscribe_2) 