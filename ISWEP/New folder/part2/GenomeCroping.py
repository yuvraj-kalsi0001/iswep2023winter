import csv

# Open the CSV file
with open('within_range.csv', newline='') as csvfile:

    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Initialize variables to store column 5 and 6 values
    prev_col5 = None
    prev_col6 = None

    # Initialize 2D list to store values
    values = []

    # Loop through the rows of the CSV file
    for row in reader:

        # Check if value in column 6 is the same as the previous row
        if row[5] == prev_col6:
            prev_col5 = row[4]
            continue

        # Add the value in column 4 to the last sublist of the 2D list
        if values and row[5] == values[-1][1]:
            # values[-1][0].append(row[3])
            print(1)
        else:
            if len(values)!=0:
                values[-1].append(prev_col5)
            values.append([row[3], row[5]])

        # Update the variable storing the previous value in column 6
        prev_col6 = row[5]
    values[-1].append(row[4])

# Print the 2D list
print(values)


# read the GFF file and get the lines within the specified indices
filename = "albidoflavus_J1074.gff"
# start_index = 10
# end_index = 20
with open(filename) as f:
    lines = f.readlines()

# extract the lines after the row containing "##FASTA"
fasta_index = None
for i, line in enumerate(lines):
    if "##FASTA" in line:
        fasta_index = i
        break
if fasta_index is None:
    print("No FASTA string found.")
    exit()
extracted_lines = lines[fasta_index+2:]

# write the extracted lines to a CSV file with the heading
# heading = ["Column1", "Column2", "Column3"]
output_filename = "output.csv"
with open(output_filename, mode='w', newline='') as f:
    writer = csv.writer(f)
    # writer.writerow(heading)
    for line in extracted_lines:
        writer.writerow(line.split('\t')[:3])  # write only the first three columns


# read the CSV file
with open('output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = []
    for row in csv_reader:
        data.append(row[-1].strip())
        # print(row[0:])
    joined_data = "".join(data)
    # print(joined_data)

# create a new GFF file
with open('output1.gff', 'w') as gff_file:
    for i in range(len(values)):
        # write the element at index 1 in the inner array
        gff_file.write(">" + str(values[i][1]) + " "+ str(values[i][0]) + "-"+ str(values[i][2]) + ' \n')
        # write the stripped string from the CSV file
        start = int(values[i][0])
        end = int(values[i][2])
        # print(len(joined_data))
        gff_file.write(joined_data[start:end] + '\n')