import csv
import os

def merge_csv_to_txt(csv_files, output_txt):
    """Merges multiple CSV files into a single TXT file.

    Args:
        csv_files (list): A list of CSV file paths.
        output_txt (str): The path of the output TXT file.
    """

    with open(output_txt, 'w', newline='') as txt_file:
        writer = csv.writer(txt_file, delimiter='\t')  # Use tab delimiter for better readability
        for csv_file in csv_files:
            with open(csv_file, 'r') as csv_file_obj:
                reader = csv.reader(csv_file_obj)
                for row in reader:
                    writer.writerow(row)

# Example usage
csv_files = ['CSV1.csv.csv', 'CSV2.csv.csv', 'CSV3.csv.csv', 'CSV4.csv.csv']
output_txt = 'merged_data.txt'
merge_csv_to_txt(csv_files, output_txt)