# Sorting Words Alphabetically

def sort_words(input_string):
    return ",".join(sorted([word.strip() for word in input_string.split(",")]))

input_string = "without,hello,bag,world"
sorted_words = sort_words(input_string)
print(sorted_words)

########################################################

# Finding the Longest Word in a Sentence

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
