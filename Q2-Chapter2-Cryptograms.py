import nltk
from nltk.corpus import words

# Download word corpus (only required once)
# nltk.download('words')

# Function to decrypt Caesar cipher with a given shift
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(((ord(char) - offset - shift) % 26) + offset)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

# Function to check if a word exists in the English dictionary
def is_english_word(word):
    english_words = set(words.words())
    return word.lower() in english_words

# Function to find the most likely shift key by checking the validity of words
def find_shift_key(ciphertext):
    for shift in range(1, 26):
        decrypted_message = decrypt_caesar_cipher(ciphertext, shift)
        word_list = decrypted_message.split()
        # Count how many words are valid English words
        valid_word_count = sum([1 for word in word_list if is_english_word(word)])
        
        # If more than half of the words are valid, this is the likely shift
        if valid_word_count > len(word_list) / 2:  # You can adjust the threshold
            return shift, decrypted_message

    # If no valid shift is found, return None
    return None, None

# Accept user input for ciphertext
ciphertext = input("Enter the ciphertext: ")

# Find the shift key and the decrypted message
shift_key, decrypted_message = find_shift_key(ciphertext)

if shift_key is not None:
    print(f"Likely Shift Key: {shift_key}")
    print(f"Decrypted Message: {decrypted_message}")
else:
    print("No valid shift key found.")
