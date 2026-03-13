
class TestSortingUsefulPage:
    
    def test_sorting_useful(self, button_sorting_useful ):  # select_tab - это название созданной фикстура
        button_sorting_useful.open()
        button_sorting_useful.click_button_sorting()
        button_sorting_useful.click_button_sorting_useful()