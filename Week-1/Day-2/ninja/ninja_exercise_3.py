# Exercise 3: From English to Morse Code

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/',
}

def english_to_morse(text):
    return ' '.join(MORSE_CODE_DICT[char] for char in text.upper() if char in MORSE_CODE_DICT)

def morse_to_english(morse_code):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict[char] for char in morse_code.split())

text = "Hello World"
morse = english_to_morse(text)
print(f"English: {text} → Morse: {morse}")

morse_text = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
english = morse_to_english(morse_text)
print(f"Morse: {morse_text} → English: {english}")
