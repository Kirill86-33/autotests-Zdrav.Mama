import pytest

class TestTabList:
    def test_tab_list(self, tab_list):
        tab_list.open()
        tab_list.click_tab_list()