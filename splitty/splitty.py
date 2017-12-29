from re import match


def clear_list_strings(strings):
    """Clear a list of strings.

    iter on a list and call split method on all substrings
    """
    return [string.strip() for string in strings if string.strip()]


def list_by_list(list_with_elements: list, list_with_intervals: list) -> list:
    """
    Split a list using another list.

    Composed function using apply_list_intervals,
        make_intervals and find_list_elements
    """
    return apply_list_intervals(list_with_elements,
                                make_intervals(
                                    find_list_elements(list_with_elements,
                                                       list_with_intervals)))

def find_list_elements(full_list, list_with_values):
    """
    Find occurrences in a list and make a index related

    TODO: Implement in declative style
    """
    intervals = []
    for x, val in enumerate(full_list):
        for y in list_with_values:
            if y == val:
                intervals.append((x, val))
    return intervals


def list_by_re_pattern(list_to_be_splited: list, pattern: 're.pattern'):
    """Find pattern occurrences in a list and make a index related."""
    return [(i, val) for i, val in enumerate(list_to_be_splited)
            if match(pattern, val)]


def make_intervals(blocks):
    """
    Make slice intervals with tuple numbers.

    iter in internal tuples and make a lists using position values

    Example:
    >>> make_intervals([(0, 'a'), (5, 'b'), (10, 'c')])
    [slice(0, 5), slice(5, 10), slice(10, None)]

    Other cases:
        case blank block:
            return [slice(1, None)]
        case block is atuple:
            transform in a list
    """
    vector = []
    if not blocks:
        vector.append(slice(1, None))
        return vector

    if isinstance(blocks[0], tuple):
        blocks = list(map(lambda x: x[0], blocks))

    for i, value in enumerate(blocks):
        if i == len(blocks) - 1:
            vector.append(slice(blocks[i], None))
        else:
            vector.append(slice(blocks[i], blocks[i + 1]))
    return vector


def apply_list_intervals(list_, intervals):
    """Apply slice lists in a list"""
    return [list_[interval] for interval in intervals]
