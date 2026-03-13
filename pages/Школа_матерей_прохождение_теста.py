from pages.base_page import BasePage

class PassingTestMothersSchoolPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/schoolmothers' 

    BUTTON_BEFORE_BIRTH = ("xpath", "//*[@id='__next']/main/div/div[2]/div[1]/div[3]/div[2]/div[1]/a")
    BUTTON_ANSWER_1 = ("xpath", "//div[text()='Развитию иммунной системы']")
    BUTTON_NEXT = ("xpath", "//div//button[text()='Далее']")
    BUTTON_ANSWER_2 = ("xpath", "//div[text()='Проблемы во взаимоотношениях со своими родителями или с партнёром']")
    BUTTON_NEXT = ("xpath", "//div//button[text()='Далее']")
    BUTTON_ANSWER_3 = ("xpath", "//div[text()='Громкая с мощными басами']")
    BUTTON_NEXT = ("xpath", "//div//button[text()='Далее']")
    BUTTON_ANSWER_4 = ("xpath", "//div[text()='Нет, поскольку отец не принимает участия в родах']")
    BUTTON_RESULT = ("xpath", "//div//button[text()='Показать результаты']")

    
    def click_button_before_birth (self):  
       button_before = self.driver.find_element(*self.BUTTON_BEFORE_BIRTH) # Добавляем явное ожидание
       self.driver.execute_script("arguments[0].click();", button_before)

        
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
