from re import match


def list_by_list(list_to_be_splited, list_with_intervals):
    """
    Split list using other list.

    TODO: Implement in declative style
    """
    intervals = []
    for x, val in enumerate(list_to_be_splited):
        for y in list_with_intervals:
            if y == val:
                intervals.append((x, val))
    return intervals


def list_by_re_pattern(list_to_be_splited, pattern):
    """Split list using a regex."""
    return [(i, val) for i, val in enumerate(list_to_be_splited)
            if match(pattern, val)]


def make_intervals(blocks):
    """
    Make slice intervals with tuple numbers.

    TODO: translate this
    CASES:
        Caso o bloco venha vazio:
            return [slice(1, None)]
        Caso o bloco seja uma tupla:
            será transformado em uma lista (pois só existe um valor)
        Caso o bloco seja uma lista, vai ser iterado entre as tuplas internas
            e será montada uma nova lista de slices entre os valores
            return [slice(x, y), slice(y, z), slice(z, None)]
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
            vector.append(slice(blocks[i], blocks[i+1]))
    return vector


def apply_list_intervals(list_, intervals):
    """Apply slice lists in a list"""
    return [list_[interval] for interval in intervals]
