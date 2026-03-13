from pages.base_page import BasePage

class PassingTestPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/quiz'

    BUTTON_PASSING_TEST = ("xpath", "(//div//a)[12]")
    BUTTON_ANSWER_1 = ("xpath", "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[4]/a")
    BUTTON_NEXT = ("xpath", "//div//button[text()='Далее']")
    BUTTON_ANSWER_2 = ("xpath", "(//div[@class='MuiBox-root css-1qp48jl'])[1]")
    BUTTON_NEXT = ("xpath", "//div//button[text()='Далее']")
    BUTTON_ANSWER_3 = ("xpath", "(//div[@class='MuiBox-root css-13c7zh5'])[1]")
    BUTTON_NEXT = ("xpath", "//div//button[text()='Далее']")
    BUTTON_ANSWER_4 = ("xpath", "(//div[@class='MuiBox-root css-13c7zh5'])[1]")
    BUTTON_RESULT = ("xpath", "//div//button[text()='Показать результаты']")



    
    def click_button_passing_test (self):  
        button_passing = self.driver.find_element(*self.BUTTON_PASSING_TEST) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_passing)

        
    def click_button_answer_1 (self):  
        button_answer_1 = self.driver.find_element(*self.BUTTON_ANSWER_1) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_answer_1)


    def click_button_next_1 (self):  
        button_next_1 = self.driver.find_element(*self.BUTTON_NEXT) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_next_1)

        
    def click_button_answer_2 (self):  
        button_answer_2 = self.driver.find_element(*self.BUTTON_ANSWER_2) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_answer_2)

        
    def click_button_next_2(self):  
        button_next_2 = self.driver.find_element(*self.BUTTON_NEXT) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_next_2)

        
    def click_button_answer_3 (self):  
        button_answer_3 = self.driver.find_element(*self.BUTTON_ANSWER_3) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_answer_3)

        
    def click_button_next_3 (self):  
        button_next_3 = self.driver.find_element(*self.BUTTON_NEXT) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_next_3)

        
    def click_button_answer_4 (self):  
        button_answer_4 = self.driver.find_element(*self.BUTTON_ANSWER_4) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();",button_answer_4)


    def click_button_result (self):  
        button_result = self.driver.find_element(*self.BUTTON_RESULT) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_result)
