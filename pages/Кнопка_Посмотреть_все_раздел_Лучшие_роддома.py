from pages.base_page import BasePage

class ButtonViewPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    BUTTON_VIEW = ("xpath", "//div//a[@class='MuiTypography-root MuiTypography-body2 MuiTypography-noWrap css-97zbqt']")



    def click_button_view(self):
        button_view = self.driver.find_element(*self.BUTTON_VIEW)
        self.driver.execute_script("arguments[0].click();", button_view)   