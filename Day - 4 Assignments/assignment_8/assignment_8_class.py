import string


class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def count_characters(self):
        return len(self.text.replace(" ", "").replace("\t", ""))

    def count_words(self):
        words = self.text.split()
        return len(words)

    def count_sentences(self):
        return self.text.count(".")

    def count_unique_words(self):
        words = self.text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        unique_words = set(words)

        return len(unique_words)

    def most_frequent_word(self):
        words = self.text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        return max(word_count, key=word_count.get)

    def longest_word(self):
        words = self.text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        return max(words, key=len)

    def shortest_word(self):
        words = self.text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        return min(words, key=len)


text = """
Python is powerful.
Python is simple.
Python is popular.
"""

analyzer = TextAnalyzer(text)

print(f"Number of characters: {analyzer.count_characters()}")
print(f"Number of words: {analyzer.count_words()}")
print(f"Number of sentences: {analyzer.count_sentences()}")
print(f"Number of unique words: {analyzer.count_unique_words()}")
print(f"Most frequently occurring word: {analyzer.most_frequent_word()}")
print(f"Longest word: {analyzer.longest_word()}")
print(f"Shortest word: {analyzer.shortest_word()}")