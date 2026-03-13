from pages.base_page import BasePage

class FieldYourCounty(BasePage):
    PAGE_URL = 'https://zdrav.mosreg.ru/widget/medical-chats'

    INPUT_YOUR_COUNTY = ("xpath", "//div//input[@placeholder='Напишите ваш городской округ']")
    BUTTON_CITY = ("xpath", "//div[text()='Балашиха']")
 
  

    def click_input_your_county (self):  
        input_city = self.driver.find_element(*self.INPUT_YOUR_COUNTY) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", input_city)


    def enter_input_your_county (self, driver):  
        input_your_county = self.driver.find_element(*self. INPUT_YOUR_COUNTY) # Добавляем явное ожидание
        input_your_county.send_keys(driver)


    def click_button_city (self):  
        button_city = self.driver.find_element(*self.BUTTON_CITY) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_city)