def process_string(s):
    # Separate numbers and letters
    number_string = ''.join([char for char in s if char.isdigit()])
    letter_string = ''.join([char for char in s if char.isalpha()])
    
    # Convert even numbers in the number string to ASCII code decimal values
    even_numbers = [int(char) for char in number_string if int(char) % 2 == 0]
    ascii_codes_from_even_numbers = [ord(str(num)) for num in even_numbers]
    
    # Convert uppercase letters in letter string to ASCII code decimal values
    uppercase_letters = [char for char in letter_string if char.isupper()]
    ascii_codes_from_uppercase = [ord(char) for char in uppercase_letters]
    
    return even_numbers, ascii_codes_from_even_numbers, uppercase_letters, ascii_codes_from_uppercase

# Prompt user for input
if __name__ == "__main__":
    input_string = input("Enter the string to process: ")
    
    even_numbers, ascii_codes_even, uppercase_letters, ascii_codes_uppercase = process_string(input_string)

    print("Even Numbers:", even_numbers)
    print("ASCII Codes (Even Numbers):", ascii_codes_even)
    print("Uppercase Letters:", uppercase_letters)
    print("ASCII Codes (Uppercase Letters):", ascii_codes_uppercase)
