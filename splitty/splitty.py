"""
Splitty.

Functional approach to work with iterables in python
"""
from re import match
from functools import singledispatch
from itertools import cycle
from numbers import Number


def clear_list_strings(strings):
    r"""
    Clear a list of strings.

    Remove newlines character in each string of a list and takes of all empty
    strings

    >>> clear_list_strings(['\r\nHello', 'how', 'r', 'u\n', '\r'])
    ['Hello', 'how', 'r', 'u']
    """
    return [string.strip() for string in strings if string.strip()]


def list_by_list(list_with_elements, list_with_intervals, start=False):
    """
    Split a list using another list.

    >>> list_with_elements = ['spam', 1, 2, 3, 'eggs', 1, 2, 3, 'foo', 1, 2, 3]

    >>> list_with_intervals = ['spam', 'eggs', 'foo']

    >>> list_by_list(list_with_elements, list_with_intervals)
    [['spam', 1, 2, 3], ['eggs', 1, 2, 3], ['foo', 1, 2, 3]]

    Composed function using apply_intervals(),
    make_intervals() and find_elements()
    """
    return apply_intervals(
        list_with_elements,
        make_intervals(
            find_elements(list_with_elements, list_with_intervals), start
        ),
    )


@singledispatch
def nun_or_match(matcher, element):
    r"""
    Discover if matcher ir a Number or String and match then.

    >>> nun_or_match(7, 7)
    True

    >>> nun_or_match('\w+', 'Hello')
    <re.Match object; span=(0, 5), match='Hello'>

    >>> nun_or_match('spam', 'spam')
    <re.Match object; span=(0, 4), match='spam'>
    """
    ...


@nun_or_match.register(str)
def str_eq(matcher, element):
    r"""
    Match strings or regex using re.match, called by nun_or_match.

    >>> nun_or_match('\w+', 'Hello')
    <re.Match object; span=(0, 5), match='Hello'>
    """
    return match(matcher, str(element))


@nun_or_match.register(Number)
def number_eq(matcher, element):
    r"""
    Match numbers , called by nun_or_match.

    >>> nun_or_match(7, 7)
    True
    """
    return matcher == element


def find_elements(full_list, list_with_values):
    """
    Find occurrences in a list and make a index related.

    >>> find_elements(['spam', 1, 2, 3, 'eggs', 1, 2, 3], ['spam', 'eggs'])
    [(0, 'spam'), (4, 'eggs')]
    """
    return [
        (x, val)
        for x, val in enumerate(full_list)
        for y in list_with_values
        if nun_or_match(y, val)
    ]


def list_by_re_pattern(list_to_be_splited, pattern, str_convert=False):
    """
    Find pattern occurrences in a list and make a index related.

    Args:
        list_to_be_splited: list with values to split with pattern
        pattern: regex pattern
        str_convert: convert all list elements to string

    Vars:
        ltbs: map_object: result of conditional of str_convert

    >>> list_to_be_splited = ['spam', 'SPAM', 'eggs', 'EGGS', 'foo', 'FOO']

    >>> regex_pattern = "[a-z]"

    >>> list_by_re_pattern(list_to_be_splited, regex_pattern)
    [(0, 'spam'), (2, 'eggs'), (4, 'foo')]
    """
    ltbs = map(str, list_to_be_splited) if str_convert else list_to_be_splited

    return [(i, val) for i, val in enumerate(ltbs) if match(pattern, val)]


def make_intervals(blocks, start=False):
    """
    Make slice intervals with tuple numbers.

    iter in internal tuples and make a lists using position values

    Args:
        blocks: List with intervals [0, 5, 10]
            if block has a list of tuples [(0, 'a'), (5, 'b'), (10, 'c')]
            use getitem to get only values like [0, 5, 10]
        start: blocks don't have start match create that

    >>> make_intervals([(0, 'a'), (5, 'b'), (10, 'c')])
    [slice(0, 5, None), slice(5, 10, None), slice(10, None, None)]
    """
    vector = []
    if not blocks:
        return [slice(0, None, None)]

    if isinstance(blocks[0], tuple):
        blocks = list(map(lambda x: x[0], blocks))

    if start:
        vector.append(slice(0, blocks[0]))

    blocks_cycle = cycle(blocks)
    next(blocks_cycle)

    middle = list(
        map(lambda block: slice(block, next(blocks_cycle)), blocks[:-1])
    )
    vector += middle

    vector.append(slice(blocks[-1], None))
    return vector


def apply_intervals(list_, intervals):
    """
    Apply slice lists in a list.

    >>> list_with_elements = ['spam', 'eggs', 'foo', 'bar']

    >>> intervals = [0, 2, 3]

    >>> apply_intervals(list_with_elements, intervals)
    ['spam', 'foo', 'bar']
    """
    return [list_[interval] for interval in intervals]


def chunks(iterable, size):
    """
    Split a iterable in chunks.

    Args:
        iterable: a list, tuple, dict or iter to be chunked
        size: size of chunks of iterable

    >>> chunks([1, 2], 1)
    [[1], [2]]

    >>> chunks([1, 2], 2)
    [[1, 2]]
    """
    return [iterable[i: i + size] for i in range(0, len(iterable), size)]
