import csv
import operator

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
        unique_set_within_range = set()
        unique_set_not_within_range = set()

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
                    
                # if (row2[0] in unique_set):
                #     continue
                
                # print(len(unique_set))
                # print(row2)

                # Check if the numbers from file1 are within the range of file2
                if num2_col3 <= num1_col4 <= num2_col4 and num2_col3 <= num1_col5 <= num2_col4:
                    # Copy data from column 3 and 5 of file2 to column 6 of file1
                    # print(row2)
                    unique_set_within_range.add(row2[0])

                    break  # Stop looping through rows in file2
                else:
                    # If the inner loop completed without finding a match, write the row to not_within_range.csv
                    if row2[0] in unique_set_within_range:
                        print()
                    else:

                        unique_set_not_within_range.add(row2[0])
        
            # Reset file2 to start from the beginning for the next row in file1
            file2.seek(0)
            next(reader2)  # Skip header row
        # Close the output files
        within_range_file.close()
        not_within_range_file.close()
print(unique_set_within_range)
print(unique_set_not_within_range)

# open the input CSV file
with open('albidoflavus_J1074-.csv', mode='r') as input_file:
    reader = csv.reader(input_file)
    
    # open the output CSV file
    with open('within_range.csv', mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        
        # loop through each row in the input CSV file
        for row in reader:
            # check if the first column element matches any element in the set
            if row[0] in unique_set_within_range:
                # write the matching row to the output CSV file
                writer.writerow(row)
    within_range_file.close()

with open('albidoflavus_J1074-.csv', mode='r') as input_file:
    reader = csv.reader(input_file)
    
    # open the output CSV file
    with open('not_within_range.csv', mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        
        # loop through each row in the input CSV file
        for row in reader:
            # check if the first column element matches any element in the set
            if row[0] in unique_set_not_within_range:
                # write the matching row to the output CSV file
                writer.writerow(row)

    within_range_file.close()


# with open('albidoflavus_J1074.csv') as file1:
#     reader1 = csv.reader(file1)
#     header1 = next(reader1)  # Save header row



#     with open('within_range.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         for i in unique_set_within_range:
#             writer.writerow([i])

#             # Close the output files
#             within_range_file.close()
#             not_within_range_file.close()       

#     with open('not_within_range.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         for i in unique_set_not_within_range:
#             writer.writerow([i])

#             # Close the output files
#             within_range_file.close()
#             not_within_range_file.close()   
