import pytest

class TestSelectPage:
    
    def test_advantages_select(self, select_tab):  # select_tab - это название созданной фикстура
        select_tab.open()
        select_tab.click_select_tab()
     
