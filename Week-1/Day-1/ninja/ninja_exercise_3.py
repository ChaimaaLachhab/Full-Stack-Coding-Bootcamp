import re
from collections import Counter

paragraph = """Python is an amazing programming language. It is widely used in web development, data science, artificial intelligence, and automation. 
Many developers love Python for its simplicity and readability. Companies like Google and Facebook use Python extensively."""

char_count = len(paragraph)

sentences = re.split(r'[.!?]', paragraph)
sentences = [s.strip() for s in sentences if s.strip()]
sentence_count = len(sentences)

words = paragraph.split()
word_count = len(words)

unique_words = set(words)
unique_word_count = len(unique_words)

non_whitespace_count = len(paragraph.replace(" ", "").replace("\n", ""))

avg_words_per_sentence = word_count / sentence_count if sentence_count else 0

word_frequencies = Counter(words)
non_unique_words_count = sum(count - 1 for count in word_frequencies.values() if count > 1)

print(f"📖 Paragraph Analysis 📖")
print(f"Total characters: {char_count}")
print(f"Total sentences: {sentence_count}")
print(f"Total words: {word_count}")
print(f"Unique words: {unique_word_count}")
print(f"Non-whitespace characters: {non_whitespace_count}")
print(f"Average words per sentence: {avg_words_per_sentence:.2f}")
print(f"Non-unique words: {non_unique_words_count}")
