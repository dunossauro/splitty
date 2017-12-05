import re
from unittest import TestCase, main
from splitty.splitty import (list_by_list, list_by_re_pattern,
                             make_intervals, apply_list_intervals)


class TestListByList(TestCase):

    def test_list_by_list(self):
        list_to_be_splited = ['spam', 1, 2, 3, 'eggs', 1, 2, 3, 'foo', 1, 2, 3]
        split_by = ['spam', 'eggs', 'foo']
        result = list_by_list(list_to_be_splited, split_by)
        assert result == [(0, 'spam'), (4, 'eggs'), (8, 'foo')]


class TestListByRePattern(TestCase):

    def test_list_by_re_pattern(self):
        list_to_be_splited = ['spam', '1', '2', '3',
                              'eggs', '1', '2', '3',
                              'foo', '1', '2', '3']
        split_by = r'(spam|eggs|f.o)'
        result = list_by_re_pattern(list_to_be_splited, split_by)
        print(result)
        assert result == [(0, 'spam'), (4, 'eggs'), (8, 'foo')]


main()
