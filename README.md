# splitty
functional approach to work with iterables in python

## Simple exaple
```python

from splitty import list_by_list, make_intervals

list_to_be_splited = ['spam', 1, 2, 3, 'eggs', 1, 2, 3, 'foo', 1, 2, 3]
split_by = ['spam', 'eggs', 'foo']

splited = list_by_list(list_to_be_splited, split_by)
# [(0, 'spam'), (4, 'eggs'), (8, 'foo')]

intervals = make_intervals(splited)
# [slice(0, 4, None), slice(4, 8, None), slice(8, None, None)]

list_with_intervals = apply_list_invervals(list_to_be_splited, intervals)
# [['spam', 1, 2, 3], ['eggs', 1, 2, 3], ['foo', 1, 2, 3]]
```
