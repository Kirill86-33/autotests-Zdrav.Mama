from pages.base_page import BasePage

class ButtonFindPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'


    BUTTON_FIND_MORE = ("xpath", "//*[@id='__next']/main/div/div/div[3]/div/div/div[1]/div[1]/a")
   

    def click_button_find(self):
        button_find = self.driver.find_element(*self.BUTTON_FIND_MORE)
        self.driver.execute_script("arguments[0].click();", button_find)


