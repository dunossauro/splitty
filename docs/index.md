[![Build Status](https://travis-ci.org/dunossauro/splitty.svg?branch=master)](https://travis-ci.org/dunossauro/splitty)
[![Coverage Status](https://coveralls.io/repos/github/dunossauro/splitty/badge.svg?branch=master)](https://coveralls.io/github/dunossauro/splitty?branch=master)
[![Waffle.io - Columns and their card count](https://badge.waffle.io/dunossauro/splitty.svg?columns=all)](https://waffle.io/dunossauro/splitty)


# splitty
functional approach to work with iterables in python

## Install
`pip install splitty`

## How do I use splitty?
You can see [examples](./examples)

### Simple example
```python

from splitty import *

>>> list_to_be_splited = ['spam', 1, 2, 3, 'eggs', 1, 2, 3, 'foo', 1, 2, 3]
>>> split_by = ['spam', 'eggs', 'foo']

>>> splited = find_elements(list_to_be_splited, split_by)
# [(0, 'spam'), (4, 'eggs'), (8, 'foo')]

>>> intervals = make_intervals(splited)
# [slice(0, 4, None), slice(4, 8, None), slice(8, None, None)]

>>> list_with_intervals = apply_intervals(list_to_be_splited, intervals)
# [['spam', 1, 2, 3], ['eggs', 1, 2, 3], ['foo', 1, 2, 3]]

# Alternative sintax to all steps
>>> list_with_intervals = list_by_list(list_to_be_splited, split_by)
# [['spam', 1, 2, 3], ['eggs', 1, 2, 3], ['foo', 1, 2, 3]]

# the same way, but using size for split
>>> chunks(list_to_be_splited, size=4)
# [['spam', 1, 2, 3], ['eggs', 1, 2, 3], ['foo', 1, 2, 3]]
```

# TODO:
- Implement documentation
- Write tests using hypotheses
- Lazy alternatives
- File manipulation objects
