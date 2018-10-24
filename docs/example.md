#Example


First of all make sure that you have the `splitty` installed, if you haven't, just run in an terminal the following command:

```
$ pip install splitty
```

If you have problems to install, talk with us, open an issue on our [github](https://github.com/dunossauro/splitty).

To execute this example you have to:

* create a directory, we will name it as `book_parsed`;
* inside this previously created directory create a file and name it as `mobydick.txt`, download the text we chose to use for this example, you can find it in our github repository in this [link](https://github.com/dunossauro/splitty/tree/master/examples/book_parsed) and put its text in the `mobydick.txt` file.

Open the python interpreter inside the created directory, `book_parsed`.

```python

>>> from splitty import (list_by_re_pattern, apply_intervals,
...                      clear_list_strings, make_intervals)
>>> 
```

If you haven't received an error you are ready to continue.

Now we are going to open the Moby Dick book saved in `mobydick.txt` and use the `clear_list_strings` function to process it cleaning the list strings.

```python

>>> with open('mobydick.txt') as text:
...     book = clear_list_strings(text.read().split('\n'))
... 
>>> 
```

We can use the `book` variable to pass it as argument to the `list_by_re_pattern` function, this one will find text occurrences using a regex pattern in all book lines. After we print the topic's list. Note that the output is simplified here, the real one is bigger.

```python

>>> numered_topics = list_by_re_pattern(book, r'CHAPTER \d{1,3}\. .*')
>>> print(numered_topics)
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
```


Another cool thing that the `splitty` lybrary offers is to make a interval lists, something like `[slice(0, 184), slice(184, 304) ...]`, and apply this intervals in all book lines. To do that we reuse the `book` and `numered_topics` variables and use them to the provided functions from the `splitty` library: `make_intervals` and `apply_intervals`. After this we join first chapter's list, and print first chapter.

```python

>>> full_book_chapter_lists = apply_intervals(book,
...                                           make_intervals(numered_topics))
>>> chapter_1 = ' '.join(full_book_chapter_lists[0])
>>> print(chapter_1)
CHAPTER 1. Loomings. Call me Ishmael. Some years ago—never mind...
...of them all, one grand hooded phantom, like a snow hill in the air.
```

Similar what was done in the first chapter, we can print the last chapter.

```python

>>> last_chapter = ' '.join(full_book_chapter_lists[-1])
>>> print(last_chapter)
CHAPTER 135. The Chase.—Third Day. The morning of the third day...
...END OF THIS PROJECT GUTENBERG EBOOK MOBY DICK; OR THE WHALE ***
```
