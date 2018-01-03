"""Splitty tests."""

from sys import path
from unittest import TestCase, main
path.append('./splitty')
from splitty import (list_by_re_pattern, find_elements,
                     list_by_list, make_intervals)


class TestFindListElements(TestCase):
    def test_find_list_elements(self):
        split_by = ['spam', 'eggs', 'foo']
        list_to_be_splited = ['spam', 1, 2, 3,
                              'eggs', 1, 2, 3,
                              'foo', 1, 2, 3]

        self.assertEqual(find_elements(list_to_be_splited, split_by),
                         [(0, 'spam'), (4, 'eggs'), (8, 'foo')])

    def test_shoud_be_blank_list_if_splited_by_blank_list(self):
        list_to_be_splited = ['spam', 1, 2, 3,
                              'eggs', 1, 2, 3,
                              'foo', 1, 2, 3]

        self.assertEqual(find_elements(list_to_be_splited, []), [])


class TestListByList(TestCase):
    def test_list_by_list(self):
        split_by = ['spam', 'eggs', 'foo']
        list_to_be_splited = ['spam', 1, 2, 3,
                              'eggs', 1, 2, 3,
                              'foo', 1, 2, 3]

        self.assertEqual(list_by_list(list_to_be_splited, split_by),
                         [['spam', 1, 2, 3],
                          ['eggs', 1, 2, 3],
                          ['foo', 1, 2, 3]])


class TestListByRePattern(TestCase):
    def test_list_by_re_pattern(self):
        split_by = r'(spam|egg(s|z)|f.o)'
        list_to_be_splited = ['spam', '1', '2', '3',
                              'eggs', '1', '2', '3',
                              'foo', '1', '2', '3']
        self.assertEqual(list_by_re_pattern(list_to_be_splited, split_by),
                         [(0, 'spam'), (4, 'eggs'), (8, 'foo')])


class Test_make_intervals(TestCase):
    def test_make_intervals(self):
        _list = list('abcdefg')
        list_to_split = list('ce')

        topics = find_elements(_list, list_to_split)

        self.assertEqual(make_intervals(topics),
                         [slice(2, 4, None),
                          slice(4, None, None)])

    def test_make_intervals_has_element_zero(self):
        _list = list('abcdefg')
        list_to_split = list('ce')

        topics = find_elements(_list, list_to_split)

        self.assertEqual(make_intervals(topics, start=True),
                         [slice(0, 2, None),
                          slice(2, 4, None),
                          slice(4, None, None)])


if __name__ == '__main__':
    main()
