import csv

# Open the first CSV file
with open('albidoflavus_J1074.csv') as file1:
    reader1 = csv.reader(file1)
    header1 = next(reader1)  # Save header row

    # Open the second CSV file
    with open('albidoflavus_J1074-.csv') as file2:
        reader2 = csv.reader(file2)
        header2 = next(reader2)  # Save header row

        # Add column headers to first file
        header1.extend(['Type', 'Most similar known cluster'])
        within_range_file = open('within_range.csv', 'w', newline='')
        not_within_range_file = open('not_within_range.csv', 'w', newline='')
        within_range_writer = csv.writer(within_range_file)
        not_within_range_writer = csv.writer(not_within_range_file)
        within_range_writer.writerow(header1)
        not_within_range_writer.writerow(header1)

        # Loop through rows in file1
        for row1 in reader1:
            # Get the numbers from columns 4 and 5
            num1_col4 = float(row1[3])
            num1_col5 = float(row1[4])

            # Loop through rows in file2
            for row2 in reader2:
                # Get the numbers from columns 3 and 4
                num2_col3 = float(row2[2])
                num2_col4 = float(row2[3])

                # Check if the numbers from file1 are within the range of file2
                if num2_col3 <= num1_col4 <= num2_col4 and num2_col3 <= num1_col5 <= num2_col4:
                    # Copy data from column 3 and 5 of file2 to column 6 of file1
                    row1.extend([row2[1], row2[4]])
                    within_range_writer.writerow(row1)
                    break  # Stop looping through rows in file2
                # else:
                #     #Copy data from column 3 and 5 of file2 to column 6 of file1
                #     row1.extend([row2[1], row2[4]])
                #     not_within_range_writer.writerow(row1)
                #     break  # Stop looping through rows in file2
            else:
                # If the inner loop completed without finding a match, write the row to not_within_range.csv
                not_within_range_writer.writerow(row1)
            # Reset file2 to start from the beginning for the next row in file1
            file2.seek(0)
            next(reader2)  # Skip header row

        # Close the output files
        within_range_file.close()
        not_within_range_file.close()

# Sorting file
# Open the CSV file for reading
with open('within_range.csv', 'r') as infile:
    reader = csv.reader(infile)

    # Skip the header row
    header = next(reader)

    # Sort the rows by the fourth column
    sorted_rows = sorted(filter(None, reader), key=lambda row: int(row[3]))

# Open the CSV file for writing
with open('within_range.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write the header row to the output file
    writer.writerow(header)

    # Write the sorted rows to the output file, skipping any blank rows
    for row in filter(None, sorted_rows):
        writer.writerow(row)

        # Open the CSV file for reading
with open('not_within_range.csv', 'r') as infile:
    reader = csv.reader(infile)

    # Skip the header row
    header = next(reader)

    # Sort the rows by the fourth column
    sorted_rows = sorted(filter(None, reader), key=lambda row: int(row[3]))

# Open the CSV file for writing
with open('not_within_range.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write the header row to the output file
    writer.writerow(header)

    # Write the sorted rows to the output file, skipping any blank rows
    for row in filter(None, sorted_rows):
        writer.writerow(row)

        
