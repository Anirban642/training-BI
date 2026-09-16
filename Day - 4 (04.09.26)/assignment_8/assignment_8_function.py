import string

def count_characters(text):
    return len(text.replace(" ", "").replace("\t", ""))

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    return text.count(".")

def count_unique_words(text):
    words = text.lower().translate(str.maketrans("", "", string.punctuation)).split()

    unique_words = set(words)

    return len(unique_words)

def most_frequent_word(text):
    words = text.lower().translate(
        str.maketrans("", "", string.punctuation)).split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return max(word_count, key=word_count.get)

def longest_word(text):
    words = text.lower().translate(
        str.maketrans("", "", string.punctuation)).split()
    return max(words, key=len)

def shortest_word(text):
    words = text.lower().translate(
        str.maketrans("", "", string.punctuation)).split()
    return min(words, key=len)

text = """
Python is powerful.
Python is simple.
Python is popular.
"""

print(f"Number of characters: {count_characters(text)}")
print(f"Number of words: {count_words(text)}")
print(f"Number of sentences: {count_sentences(text)}")
print(f"Number of unique words: {count_unique_words(text)}")
print(f"Most frequent word: {most_frequent_word(text)}")
print(f"Longest word: {longest_word(text)}")
print(f"Shortest word: {shortest_word(text)}")