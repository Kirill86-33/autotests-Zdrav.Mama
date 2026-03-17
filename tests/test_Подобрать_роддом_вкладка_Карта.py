from testit_python_commons.decorators import externalId, displayName

class TestTabList:
    @externalId("test_tab_list_map")
    @displayName("Вкладка 'Карта'")
    def test_tab_list(self, tab_map):
        tab_map.open()
        tab_map.click_tab_map()