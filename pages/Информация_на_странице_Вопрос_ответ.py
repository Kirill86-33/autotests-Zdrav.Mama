from pages.base_page import BasePage

class ButtonInformationPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/faq'


    BUTTON_INFORMATION = ("xpath", "//div//h5[text()='Что взять в роддом роженице?']")


    def click_button_information(self):
        button_information = self.driver.find_element(*self.BUTTON_INFORMATION)
        self.driver.execute_script("arguments[0].click();", button_information)