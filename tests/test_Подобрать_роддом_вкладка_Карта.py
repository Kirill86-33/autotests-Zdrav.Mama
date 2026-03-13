import pytest

class TestTabList:
    def test_tab_list(self, tab_map):
        tab_map.open()
        tab_map.click_tab_map()