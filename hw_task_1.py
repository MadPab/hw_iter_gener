class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index_current_list = 0
        self.index_in_list = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index_current_list < len(self.list_of_list):
            if self.index_in_list < len(self.list_of_list[self.index_current_list]):
                item = self.list_of_list[self.index_current_list][self.index_in_list]
                self.index_in_list += 1
                return item
            self.index_current_list += 1
            self.index_in_list = 0
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    print("Test passed successfully")

if __name__ == '__main__':
    test_1()
