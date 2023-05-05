import os
import csv

# Define the directory containing the CSV files
directory = "D:\MUN\winter2023\ISWEP\gc\col3copy"

# Define the output file name
output_file = "output.csv"

# Create a dictionary to store the data
data_dict = {}

# Loop through all files in the directory
for file_name in os.listdir(directory):

    # Check if the file is a CSV file
    if file_name.endswith(".csv"):

        # Open the file and read the data
        with open(os.path.join(directory, file_name), "r") as in_csv:
            reader = csv.reader(in_csv)

            # Get the header row
            header_row = next(reader)

            # Loop through the data and store column 3 in the dictionary
            for row in reader:
                try:
                    if file_name not in data_dict:
                        data_dict[file_name] = [row[2]]
                    else:
                        data_dict[file_name].append(row[2])
                except IndexError:
                    if file_name not in data_dict:
                        data_dict[file_name] = [""]
                    else:
                        data_dict[file_name].append("")

# Open the output file in write mode
with open(output_file, "w", newline="") as out_csv:
    writer = csv.writer(out_csv)

    # Write the header row
    header = ["File Name"]
    for file_name in data_dict.keys():
        header.append(file_name)
    writer.writerow(header)

    # Write the data rows
    for i in range(len(list(data_dict.values())[0])):
        row = [i+1]
        for file_name in data_dict.keys():
            try:
                row.append(data_dict[file_name][i])
            except IndexError:
                row.append("")
        writer.writerow(row)

print("CSV file created successfully!")
