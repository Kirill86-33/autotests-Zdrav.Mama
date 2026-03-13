import pytest

class TestTabPage:
    
    def test_tab_page(self,  button_tab_test ):  # select_tab - это название созданной фикстура
         button_tab_test.open()
         button_tab_test.click_tab_test()