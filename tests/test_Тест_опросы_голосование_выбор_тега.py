from testit_python_commons.decorators import externalId, displayName

class TestTabPage:
    @externalId("test_tab_page")
    @displayName("Вкладка теста")
    def test_tab_page(self,  button_tab_test ):  # select_tab - это название созданной фикстура
         button_tab_test.open()
         button_tab_test.click_tab_test()