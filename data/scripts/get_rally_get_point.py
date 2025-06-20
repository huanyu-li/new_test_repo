import csv
import sys


def filter_and_save_csv(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)
        index = 0
        for row in csv_reader:
            # Example condition: Keep rows where the first column is 'True'
            if index == 0:
                csv_writer.writerow(row)
            else:
                if len(row[21]) > 0:
                    csv_writer.writerow(row)
            index+=1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    
    filter_and_save_csv(input_file_path, output_file_path)
