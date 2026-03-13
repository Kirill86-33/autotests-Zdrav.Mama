from pages.base_page import BasePage

class SearchCity(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/clinics'

    BUTTON_LIST = ("xpath", "//div//button[text()='Список']")
    INPUT_CITY = ("xpath", "//*[@id=':r2:']")
    BUTTON_CITY = ("xpath", "(//div//label)[1]")
    MAP_LPU = ("xpath", "(//div//a)[11]")

    

    def click_button_list(self):
        button_list = self.driver.find_element(*self.BUTTON_LIST)
        self.driver.execute_script("arguments[0].click();", button_list) 
    

    def enter_input_city (self, driver):  
        input_city = self.driver.find_element(*self.INPUT_CITY) # Добавляем явное ожидание
        input_city.send_keys(driver)


    def click_button_city(self):
        button_city = self.driver.find_element(*self.BUTTON_CITY)
        self.driver.execute_script("arguments[0].click();", button_city) 
    
    
    def click_map_lpu(self):
        button_map_lpu = self.driver.find_element(*self.MAP_LPU)
        self.driver.execute_script("arguments[0].click();", button_map_lpu) 