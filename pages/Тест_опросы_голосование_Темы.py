from pages.base_page import BasePage

class ButtonChoosingPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/quiz'


    BUTTON_SELECTING_TOPIC = ("xpath", "//div//span[text()='Беременность']")
   

    def click_button_topic(self):
        button_topic = self.driver.find_element(*self.BUTTON_SELECTING_TOPIC)
        self.driver.execute_script("arguments[0].click();", button_topic)