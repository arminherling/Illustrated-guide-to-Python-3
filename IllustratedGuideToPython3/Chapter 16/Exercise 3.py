# Exercise: Write a paragraph in a triple-quoted string. Use the .split method to create a list of
# words. Create a dictionary to hold the count for every word in the paragraph.

import collections

emerson_poem = """Daughters of Time, the hypocritic Days,
Muffled and dumb like barefoot dervishes,
And marching single in an endless file,
Bring diadems and fagots in their hands.
To each they offer gifts after his will,
Bread, kingdom, stars, and sky that holds them all.

I, in my pleached garden, watched the pomp,
Forgot my morning wishes, hastily
Took a few herbs and apples, and the Day
Turned and departed silent. I, too late,
Under her solemn fillet saw the scorn."""

list_of_words = emerson_poem.split()
word_count = collections.Counter(list_of_words)

print(word_count)