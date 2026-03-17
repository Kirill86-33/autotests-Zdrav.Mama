from testit_python_commons.decorators import externalId, displayName

class TestTabList:
    @externalId("test_tab_list_list")
    @displayName("Вкладка 'Список'")
    def test_tab_list(self, tab_list):
        tab_list.open()
        tab_list.click_tab_list()