# 🌟 Challenge 1 : Remove Duplicates

def remove_consecutive_duplicates(word):

    # Start with the first character
    result = word[0]
    for i in range(1, len(word)):

        # Add if different from the previous character
        if word[i] != word[i - 1]:
            result += word[i]
    return result

# Ask the user to enter a word
user_input = input("Enter a word: ")

# Remove consecutive duplicates and display the result
cleaned_word = remove_consecutive_duplicates(user_input)
print("Word without duplicates:", cleaned_word)
