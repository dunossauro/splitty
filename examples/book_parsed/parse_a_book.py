from splitty import (list_by_re_pattern, apply_intervals,
                     clear_list_strings, make_intervals)


# Open Moby Dick book
with open('examples/book_parsed/mobydick.txt') as text:
    # book receives non-blanklines strings
    book = clear_list_strings(text.read().split('\n'))

# Find text ocurrences using a regex pattern in all book lines
numered_topics = list_by_re_pattern(book, r'CHAPTER \d{1,3}\. .*')

# Print topic's list
print(numered_topics)
"""
[(0, 'CHAPTER 1. Loomings.'),
 (184, 'CHAPTER 2. The Carpet-Bag.'),
 (304, 'CHAPTER 3. The Spouter-Inn.'),
 (798, 'CHAPTER 4. The Counterpane.'),
 (933, 'CHAPTER 5. Breakfast.'),
 (1000, 'CHAPTER 6. The Street.'),
 ...
 ...
 (17687, 'CHAPTER 134. The Chase—Second Day.'),
 (17976, 'CHAPTER 135. The Chase.—Third Day.')]
"""

# Use regex to find topics and make a interval lists
# Something like '[slice(0, 184), slice(184, 304) ...]'
# And apply this intervals in all book lines
full_book_chapter_lists = apply_intervals(book,
                                          make_intervals(numered_topics))

# Join first chapter's list
chapter_1 = ' '.join(full_book_chapter_lists[0])

# Print First Chapter
print(chapter_1)
"""
CHAPTER 1. Loomings. Call me Ishmael. Some years ago—never mind...
...of them all, one grand hooded phantom, like a snow hill in the air.
"""

# Join last chapter's list
last_chapter = ' '.join(full_book_chapter_lists[-1])

# Print First Chapter
print(last_chapter)
"""
CHAPTER 135. The Chase.—Third Day. The morning of the third day...
...END OF THIS PROJECT GUTENBERG EBOOK MOBY DICK; OR THE WHALE ***
"""
