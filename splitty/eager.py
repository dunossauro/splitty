from toolz import compose
from .splitty import (clear_list_strings,
                      list_by_list,
                      find_elements,
                      list_by_re_pattern,
                      make_intervals,
                      apply_intervals,
                      chunks)

clear_list_strings = compose(list, clear_list_strings)
list_by_list = compose(list, list_by_list)
find_elements = compose(list, find_elements)
list_by_re_pattern = compose(list, list_by_re_pattern)
make_intervals = compose(list, make_intervals)
apply_intervals = compose(list, apply_intervals)
chunks = compose(list, chunks)
