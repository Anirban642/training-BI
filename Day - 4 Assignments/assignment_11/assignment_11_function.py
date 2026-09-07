import string

def get_word_frequency(text):
    if not text.strip():
        raise ValueError("Input cannot be empty")
    words = text.lower().translate(str.maketrans("", "", string.punctuation)).split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

def get_most_common_word(text):
    word_frequency = get_word_frequency(text)
    return max(word_frequency, key=word_frequency.get)

def get_unique_words(text):
    word_frequency = get_word_frequency(text)
    unique_words = {}
    for word in word_frequency:
        if word_frequency[word] == 1:
            unique_words[word] = 1
    return unique_words

text = """
Python is easy.
Python is powerful.
Python is widely used.
"""

try:
    print("Word Frequency:", get_word_frequency(text))
    print("Most Common Word:", get_most_common_word(text))
    print("Unique Words:", get_unique_words(text))
except ValueError as e:
    print(e)