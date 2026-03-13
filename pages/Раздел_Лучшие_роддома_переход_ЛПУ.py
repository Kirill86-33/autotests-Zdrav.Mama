from pages.base_page import BasePage

class ButtonHospitalPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    BUTTON_MATERNITY_HOSPITAL = ("xpath", "//div//a[@class='MuiBox-root css-1tx3ekz']")



    def click_button_hospital(self):
        button_hospital = self.driver.find_element(*self.BUTTON_MATERNITY_HOSPITAL)
        self.driver.execute_script("arguments[0].click();", button_hospital)   