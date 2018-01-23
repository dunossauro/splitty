from splitty import (list_by_re_pattern, apply_intervals,
                     clear_list_strings, make_intervals)

# Open moby dick book
with open('examples/book_parsed/mobydick.txt') as text:
    # book recive a non-blanklines strings
    book = clear_list_strings(text.read().split('\n'))

# Find re ocurrences (using a regex) in all line lists
numered_topics = list_by_re_pattern(book, r'CHAPTER \d{1,3}\. .*')
"""
[(0, 'CHAPTER 1. Loomings.'),
 (184, 'CHAPTER 2. The Carpet-Bag.'),
 (304, 'CHAPTER 3. The Spouter-Inn.'),
 (798, 'CHAPTER 4. The Counterpane.'),
 (933, 'CHAPTER 5. Breakfast.'),
 (1000, 'CHAPTER 6. The Street.'),
 (1074, 'CHAPTER 7. The Chapel.'),
 (1156, 'CHAPTER 8. The Pulpit.'),
 (1239, 'CHAPTER 9. The Sermon.'),
 (1537, 'CHAPTER 10. A Bosom Friend.'),
"""

# Use regex finded topics and make a interval lists
# somithng like [slice(0, 184), slice(184, 304) ...]
# And apply this intervals in all book lines
full_book_chapter_lists = apply_intervals(book,
                                          make_intervals(numered_topics))

# join first chapter lists
chapter_1 = ' '.join(full_book_chapter_lists[0])

print(chapter_1)
"""
CHAPTER 1. Loomings. Call me Ishmael. ... like a snow hill in the air.
"""

last_chapter = ' '.join(full_book_chapter_lists[-1])

# join last chapter lists
print(last_chapter)
"""
CHAPTER 135. The Chase.—Third Day. The morning of the third day dawned fair
...
*** END OF THIS PROJECT GUTENBERG EBOOK MOBY DICK; OR THE WHALE ***
"""
