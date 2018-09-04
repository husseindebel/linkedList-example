import pytest
from List import List 

class TestUS1(object):

    def setup_method(self):
        self.list = List()

    def test_new(self):
        assert self.list.head == None

    def test1_new1(self):
        self.list.add_item(8)
        self.list.add_item(9)
        self.list.add_item(10)
        self.list.add_item(11)

        assert self.list.size == 4
        assert self.list.contains(8) == True
        assert self.list.contains(9) == True
        assert self.list.contains(10) == True
        assert self.list.contains(11) == True
        assert self.list.contains(12) == False
        # print(self.list.to_list)
        assert self.list.to_list == [8,9,10,11]

    # def teardown_method(self):
    #     pass

    # def setup_class(self):
    #     pass

    # def teardown_class(self):
    #     pass

    # def test_view_items(self):
    #     items = self.system.display_menu()
    #     assert len(items) == 3
    #     assert items[0].name == "Burger"
    #     assert items[1].name == "Salad"
    #     assert items[2].name == "Mocha"
    #     assert items[0].price == 20
    #     assert items[1].price == 15
    #     assert items[2].price == 10
    #     assert items[0].availability is True
    #     assert items[1].availability is False
    #     assert items[2].availability is True

    # def test_check_item_empty_name(self):
    #     error = self.system.display_item("")
    #     assert error == "Item name is empty"

    # def test_check_item_wrong_name(self):
    #     error = self.system.display_item("Barger")
    #     assert error == "Item doesn't exist"

    # def test_check_item_successful(self):
    #     item = self.system.display_item("Burger")
    #     assert isinstance(item, Item)
    #     assert item.name == "Burger"
    #     assert item.price == 20
    #     assert item.availability is True
    #     assert item.ingredients == ["Lettuce", "Tomato", "Beef"]

    # def test_check_item_tags(self):
    #     item = self.system.display_item("Burger")
    #     assert isinstance(item, Item)
    #     assert item.tags == ["nut-free"]


