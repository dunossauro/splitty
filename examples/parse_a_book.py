from operator import getitem
from pprint import pprint
from splitty import list_by_re_pattern, list_by_list, clear_list_strings

with open('examples/mobydick.txt') as text:
    book = clear_list_strings(text.read().split('\n'))

numered_topics = list_by_re_pattern(book, r'CHAPTER \d{1,3}\. .*')
"""Result.
    [(47, 'CHAPTER 1. Loomings.'),
     (49, 'CHAPTER 2. The Carpet-Bag.'),
     (51, 'CHAPTER 3. The Spouter-Inn.'),
     (53, 'CHAPTER 4. The Counterpane.'),
     (55, 'CHAPTER 5. Breakfast.'), ... ,]
"""
topics = [getitem(x, 1) for x in numered_topics]

pprint(topics)
"""
Topics
'CHAPTER 1. Loomings.',
 'CHAPTER 2. The Carpet-Bag.',
 'CHAPTER 3. The Spouter-Inn.',
 'CHAPTER 4. The Counterpane.',
 'CHAPTER 5. Breakfast.',
 'CHAPTER 6. The Street.',
 ...
 'CHAPTER 135. The Chase.—Third Day.
"""

pprint(list_by_list(book, topics)[-1])
"""
'CHAPTER 135. The Chase.—Third Day.',
 'The morning of the third day dawned fair and fresh, and once more the',
 'solitary night-man at the fore-mast-head was relieved by crowds of the',
 'daylight look-outs, who dotted every mast and almost every spar.',
 ...
  '  http://www.gutenberg.org',
 'This Web site includes information about Project Gutenberg-tm,',
 'including how to make donations to the Project Gutenberg Literary',
 'Archive Foundation, how to help produce our new eBooks, and how to',
 'subscribe to our email newsletter to hear about new eBooks.']
 """
