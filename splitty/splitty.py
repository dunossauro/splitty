"""
Splitty.

functional approach to work with iterables in python
"""
from re import match


def clear_list_strings(strings: list) -> list:
    r"""
    Clear a list of strings.

    Remove newlines character in each string of a list and takes of all empty
    strings

    >>> clear_list_strings(['\r\nHello', 'how', 'r', 'u\n', '\r'])
    ['Hello', 'how', 'r', 'u']
    """
    return [string.strip() for string in strings if string.strip()]


def list_by_list(list_with_elements: list,
                 list_with_intervals: list,
                 start=False) -> list:
    """
    Split a list using another list.

    Composed function using apply_list_intervals,
        make_intervals and find_list_elements
    """
    return apply_intervals(list_with_elements,
                           make_intervals(
                               find_elements(list_with_elements,
                                             list_with_intervals), start))


def find_elements(full_list: list, list_with_values: list) -> list:
    """
    Find occurrences in a list and make a index related.

    >>> find_elements(['spam', 1, 2, 3, 'eggs', 1, 2, 3], ['spam', 'eggs'])
    [(0, 'spam'), (4, 'eggs')
    """
    return [(x, val) for x, val in enumerate(full_list)
            for y in list_with_values
            if y == val]


def list_by_re_pattern(list_to_be_splited: list,
                       pattern: 'pattern',
                       str_convert: bool = False) -> list:
    """
    Find pattern occurrences in a list and make a index related.

    Args:
        list_to_be_splited: list with values to split with pattern
        pattern: regex pattern
        str_convert: convert all list elements to string

    Vars:
        ltbs: map_object: result of conditional of str_convert
    """
    ltbs = map(str, list_to_be_splited) if str_convert else list_to_be_splited

    return [(i, val) for i, val in enumerate(ltbs)
            if match(pattern, val)]


def make_intervals(blocks: list, start: bool = False) -> list:
    """
    Make slice intervals with tuple numbers.

    iter in internal tuples and make a lists using position values

    Args:
        blocks: List with intervals [0, 5, 10]
            if block has a list of tuples [(0, 'a'), (5, 'b'), (10, 'c')]
            use getitem to get only values like [0, 5, 10]
        start: blocks don't have start match create that

    Example:
    >>> make_intervals([(0, 'a'), (5, 'b'), (10, 'c')])
    [slice(0, 5), slice(5, 10), slice(10, None)]
    """
    vector = []
    if not blocks:
        return [slice(0, None, None)]

    if isinstance(blocks[0], tuple):
        blocks = list(map(lambda x: x[0], blocks))

    for i, _ in enumerate(blocks):
        if start and i == 0:
            vector.append(slice(0, blocks[i]))
        if i == len(blocks) - 1:
            vector.append(slice(blocks[i], None))
        else:
            vector.append(slice(blocks[i], blocks[i + 1]))
    return vector


def apply_intervals(list_: list, intervals: list) -> list:
    """Apply slice lists in a list."""
    return [list_[interval] for interval in intervals]


def chunks(iterable: iter, size: int) -> list:
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
