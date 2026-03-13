from pages.base_page import BasePage

class ButtonCatalogPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'


    BUTTON_CATALOG = ("xpath", "//*[@id='__next']/main/div/div/div[3]/div/div/div[1]/div[2]/a")


    def click_button_catalog(self):
        button_catalog = self.driver.find_element(*self.BUTTON_CATALOG)
        self.driver.execute_script("arguments[0].click();", button_catalog)