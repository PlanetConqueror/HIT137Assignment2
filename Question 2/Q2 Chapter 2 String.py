# Given string
s = '56aAww1984sktr235270aYmm145ss785fsq31D0'

# Step 1: Separate numbers and letters
numbers = ''.join([char for char in s if char.isdigit()])
letters = ''.join([char for char in s if char.isalpha()])

# Step 2: Extract even numbers and uppercase letters
even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
uppercase_letters = [char for char in letters if char.isupper()]

# Step 3: Convert even numbers to ASCII codes
even_numbers_ascii = [ord(str(num)) for num in even_numbers]

# Step 4: Convert uppercase letters to ASCII codes
uppercase_letters_ascii = [ord(char) for char in uppercase_letters]

# Display the results
print(f"Numbers in the string: {numbers}")
print(f"Even numbers: {even_numbers}")
print(f"ASCII codes for even numbers: {even_numbers_ascii}")

print(f"Letters in the string: {letters}")
print(f"Uppercase letters: {uppercase_letters}")
print(f"ASCII codes for uppercase letters: {uppercase_letters_ascii}")
