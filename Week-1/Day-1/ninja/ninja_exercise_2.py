longest_sentence = ""
print("Try to type the longest sentence you can without using the letter 'A'!")

while True:
    sentence = input("Enter your sentence: ")
    
    if 'A' in sentence.upper():
        print("Oops! Your sentence contains the letter 'A'. Try again.")
    elif len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print(f"Congratulations! New longest sentence recorded: {len(sentence)} characters.")
    else:
        print(f"Nice try! Your sentence had {len(sentence)} characters, but the longest is {len(longest_sentence)} characters.")
