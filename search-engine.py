# You’re working on a search engine. Watch your back Google!
# The given code takes a text and a word as input and passes them to a function called search().
# The search() function should return "Word found" if the word is present in the text, or "Word not found",
# if it’s not.

def search(text, word):
    """Search engine"""
    # look whether the word is in the text provided
    if word in text:
        print('Word found')
    else:
        print('Word not found')


text = input()
word = input()
search(text, word)