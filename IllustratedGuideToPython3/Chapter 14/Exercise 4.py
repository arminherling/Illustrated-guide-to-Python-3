# Exercise: Go to Project Gutenberg and find a page of text from Shakespeare. Paste it into a
# triple-quoted string. Create another string with a paragraph of text from Ralph Waldo
# Emerson. Use the string’s .split method to get a list of words from each. Using set
# operations find the common words and words unique to both authors.

shakespeare_text = """'They met me in the day of success: and I have
learned by the perfectest report, they have more in
them than mortal knowledge. When I burned in desire
to question them further, they made themselves air,
into which they vanished. Whiles I stood rapt in
the wonder of it, came missives from the king, who
all-hailed me 'Thane of Cawdor;' by which title,
before, these weird sisters saluted me, and referred
me to the coming on of time, with 'Hail, king that
shalt be!' This have I thought good to deliver
thee, my dearest partner of greatness, that thou
mightst not lose the dues of rejoicing, by being
ignorant of what greatness is promised thee. Lay it
to thy heart, and farewell.'
Glamis thou art, and Cawdor; and shalt be
What thou art promised: yet do I fear thy nature;
It is too full o' the milk of human kindness
To catch the nearest way: thou wouldst be great;
Art not without ambition, but without
The illness should attend it: what thou wouldst highly,
That wouldst thou holily; wouldst not play false,
And yet wouldst wrongly win: thou'ldst have, great Glamis,
That which cries 'Thus thou must do, if thou have it;
And that which rather thou dost fear to do
Than wishest should be undone.' Hie thee hither,
That I may pour my spirits in thine ear;
And chastise with the valour of my tongue
All that impedes thee from the golden round,
Which fate and metaphysical aid doth seem
To have thee crown'd withal."""

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

shakespeare_words = set(shakespeare_text.split())
emerson_words = set(emerson_poem.split())

common_words = shakespeare_words & emerson_words
unique_words = shakespeare_words ^ emerson_words
print("Common words:", common_words)
print("Unique words:", unique_words)