import string

class WordFrequencyAnalyzer:
    def __init__(self, text):
        self.text = text

    def get_word_frequency(self):
        if not self.text.strip():
            raise ValueError("Input cannot be empty")
        words = self.text.lower().translate(str.maketrans("", "", string.punctuation)).split()
        word_frequency = {}
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
        return word_frequency

    def get_most_common_word(self):
        word_frequency = self.get_word_frequency()
        return max(word_frequency, key=word_frequency.get)

    def get_unique_words(self):
        word_frequency = self.get_word_frequency()
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

analyzer = WordFrequencyAnalyzer(text)

try:
    print("Word Frequency:", analyzer.get_word_frequency())
    print("Most Common Word:", analyzer.get_most_common_word())
    print("Unique Words:", analyzer.get_unique_words())
except ValueError as e:
    print(e)