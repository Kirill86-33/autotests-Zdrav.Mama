from testit_python_commons.decorators import externalId, displayName
class TestSortingUsefulPage:
    @externalId("test_sorting_useful")
    @displayName("Сортировка полезного")
    def test_sorting_useful(self, button_sorting_useful ):  # select_tab - это название созданной фикстура
        button_sorting_useful.open()
        button_sorting_useful.click_button_sorting()
        button_sorting_useful.click_button_sorting_useful()