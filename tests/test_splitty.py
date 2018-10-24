"""Splitty tests."""

from unittest import TestCase, main
from splitty import *  # NOQA


class TestInit(TestCase):
    def test_module_shouldnt_call_functions_out_all(self):
        import splitty
        with self.assertRaises(AttributeError):
            splitty.nun_or_match()


class TestNunOrMatch(TestCase):
    def setUp(self):
        from splitty.splitty import nun_or_match
        self.nom = nun_or_match

    def test_num_or_match_should_return_True_when_mach_same_number(self):
        self.assertTrue(self.nom(7, 7))

    def test_num_or_match_should_return_False_when_mach_different_number(self):
        self.assertFalse(self.nom(7, 8))

    def test_num_or_match_should_return_regex_match_when_compare_strings(self):
        import re, sys, _sre

        if sys.version_info[1] >= 7:
            self.assertIsInstance(self.nom('sa', 'sa'), re.Match)

    def test_num_or_match_should_return_regex_match_when_non_match_regex(self):
        self.assertIsNone(self.nom('sa', 's1a'))


class TestFindListElements(TestCase):
    def test_find_list_should_return_positions_and_strings(self):
        split_by = ['spam', 'eggs', 'foo']
        list_to_be_splited = [
            'spam', 1, 2, 3,
            'eggs', 1, 2, 3,
            'foo', 1, 2, 3
        ]
        self.assertEqual(find_elements(list_to_be_splited, split_by),
                         [(0, 'spam'), (4, 'eggs'), (8, 'foo')])

    def test_find_list_should_return_positions_and_strings_with_regex(self):
        split_by = [r'spa\w', r'\wggs', r'f\wo', r'b.r']
        list_to_be_splited = [
            'spam', 1, 2, 3,
            'eggs', 1, 2, 3,
            'foo', 1, 2, 3,
            'bar', 1, 2, 3
        ]
        self.assertEqual(find_elements(list_to_be_splited, split_by),
                         [(0, 'spam'), (4, 'eggs'), (8, 'foo'), (12, 'bar')])

    def test_find_list_should_return_positions_and_strings_with_mixin_regex_and_string(self):
        split_by = [r'spa\w', 'eggs', r'f\wo', 'bar']
        list_to_be_splited = [
            'spam', 1, 2, 3,
            'eggs', 1, 2, 3,
            'foo', 1, 2, 3,
            'bar', 1, 2, 3
        ]
        self.assertEqual(find_elements(list_to_be_splited, split_by),
                         [(0, 'spam'), (4, 'eggs'), (8, 'foo'), (12, 'bar')])

    def test_should_be_blank_list_if_splited_by_blank_list(self):
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

    def test_dont_parse_if_has_non_string_value_in_iterable(self):
        split_by = r'(spam|egg(s|z)|f.o)'
        list_to_be_splited = ['spam', 1, 2, 3,
                              'eggs', '1', '2', '3',
                              'foo', '1', '2', '3']

        with self.assertRaises(TypeError):
            list_by_re_pattern(list_to_be_splited, split_by)

    def test_parse_if_has_non_string_value_in_iterable_with_str_convert(self):
        split_by = r'(spam|egg(s|z)|f.o)'
        list_to_be_splited = ['spam', 1, 2, 3,
                              'eggs', '1', '2', '3',
                              'foo', '1', '2', '3']

        self.assertEqual(list_by_re_pattern(list_to_be_splited,
                                            split_by,
                                            True),
                         [(0, 'spam'), (4, 'eggs'), (8, 'foo')])


class TestMakeIntervals(TestCase):
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

    def test_make_intervals_return_blank_if_input_blank(self):
        self.assertEqual(make_intervals([]), [slice(0, None, None)])

    def test_make_intervals_using_a_list_with_values(self):
        self.assertEqual(make_intervals([1, 2, 3, 4]),
                         [slice(1, 2, None),
                          slice(2, 3, None),
                          slice(3, 4, None),
                          slice(4, None, None)])


class TestChunks(TestCase):
    def test_chunk_should_be_one_list_by_value(self):
        _list = list('abcdefg')

        self.assertEqual(chunks(_list, 1),
                         [['a'], ['b'], ['c'],
                          ['d'], ['e'], ['f'],
                          ['g']])

    def test_internal_lists_should_be_the_same_of_n(self):
        _list = list('abcdefg')
        n = 1
        result = chunks(_list, n)
        for chunk in result:
            self.assertEqual(len(chunk), n)

    def test_last_internal_lists_should_be_less_than_n(self):
        _list = list('abcdefg')
        n = 2
        result = chunks(_list, n)
        last = result[-1]

        self.assertLess(len(last), n)

    def test_internals_should_be_less_than_n_if_n_is_greater_than_size(self):
        _list = list('abcdefg')
        n = 10
        result = chunks(_list, n)

        self.assertLess(len(result), n)


class TestClearListString(TestCase):
    def test_should_remove_blank_lines(self):
        _list = ['\r\nHello', 'how', '\r', 'r', 'u\n', '\r']
        expected = ['Hello', 'how', 'r', 'u']
        self.assertEqual(clear_list_strings(_list), expected)
