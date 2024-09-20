import collections
import csv

# Function to count words and write to CSV
def count_and_write_top_words(input_file, output_csv):
    # Read the text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize words (assuming basic splitting by whitespace)
    words = text.split()

    # Count occurrences of each word
    word_counts = collections.Counter(words)

    # Get the top 30 most common words
    top_30_words = word_counts.most_common(30)

    # Write the top 30 words and their counts to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as isfile:
        csv_writer = csv.writer(isfile)
        csv_writer.writerow(['Word', 'Count'])
        csv_writer.writerows(top_30_words)

    print(f"Top 30 words and their counts have been written to '{output_csv}'.")

# Example usage:
input_file = 'merged_data.txt'  
output_csv = 'top_30_words.csv'   

count_and_write_top_words(input_file, output_csv)