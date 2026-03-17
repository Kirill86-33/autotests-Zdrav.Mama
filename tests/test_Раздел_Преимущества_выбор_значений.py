from testit_python_commons.decorators import externalId, displayName

class TestSelectPage:
    @externalId("test_advantages_select")
    @displayName("Выбор преимуществ")
    def test_advantages_select(self, select_tab):  # select_tab - это название созданной фикстура
        select_tab.open()
        select_tab.click_select_tab()
     
