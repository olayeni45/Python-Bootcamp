import csv
# Other Libraries: Pandas, Openpyxl, Google Sheets Python API

# Open the File
# CSV.Reader
# Reformat it into a python object

data = open("example.csv", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

column_names = data_lines[0]
all_emails = [line[3] for line in data_lines[1:]] #[1:] means ignore the first row
full_names = [f"{line[1]} {line[2]}" for line in data_lines[1:]]

file_to_output = open("to_save_file.csv", mode="w", newline="")
csv_writer = csv.writer(file_to_output, delimiter=",")
csv_writer.writerow(['a', 'b', 'c']) # Columns
csv_writer.writerows([
    ['1', '2', '3'],
    ['4', '5', '6']
])
file_to_output.close()