# splitty
functional approach to work with iterables in python

## Install
`pip install splitty`

## How I use splitty?
You can see [examples](./examples)

### Simple example
```python

from splitty import *

list_to_be_splited = ['spam', 1, 2, 3, 'eggs', 1, 2, 3, 'foo', 1, 2, 3]
split_by = ['spam', 'eggs', 'foo']

splited = find_elements(list_to_be_splited, split_by)
# [(0, 'spam'), (4, 'eggs'), (8, 'foo')]

intervals = make_intervals(splited)
# [slice(0, 4, None), slice(4, 8, None), slice(8, None, None)]

list_with_intervals = apply_intervals(list_to_be_splited, intervals)
# [['spam', 1, 2, 3], ['eggs', 1, 2, 3], ['foo', 1, 2, 3]]

# Alternative sintax to all steps
list_with_intervals = list_by_list(list_to_be_splited, split_by)
# [['spam', 1, 2, 3], ['eggs', 1, 2, 3], ['foo', 1, 2, 3]]
```

# TODO:
- Implement documentation
- Write tests using hypotheses
