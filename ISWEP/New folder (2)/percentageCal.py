import pandas as pd
import csv
from proteinCount import proteinCount
from countOccurances import countOccurances
import matplotlib.pyplot as plt
import numpy as np


inputFilep1 = "akebiae_proteins_la" 
outputfilep1 = inputFilep1 + "_protiein_count.csv"
inputFilep2 = "akebiae_proteins_le"
outputfilep2 = inputFilep2 + "_protiein_count.csv"

proteinCount(inputFilep1 + ".fasta", outputfilep1)

proteinCount(inputFilep2 + ".fasta", outputfilep2)

outputFileForCO1 = inputFilep1 + "_Count_occurance.csv"
outputFileForCO2 = inputFilep2 + "_Count_occurance.csv"

countOccurances(outputfilep1,outputFileForCO1)
countOccurances(outputfilep2,outputFileForCO2)


# Read CSV file
df = pd.read_csv(outputFileForCO1)


# Determine the maximum value in column 1 and set that as the upper bound of the last interval range
max_val = df.iloc[:, 0].max()
interval_ranges =[]
startN = 0
endN = 100
difference = 100
while(True):
    interval_ranges.append((startN, endN))
    if (endN > max_val):
        break
    startN = endN + 1
    endN = endN + difference

# print(interval_ranges)

# Initialize a dictionary to store the occurrence counts
occurrences = {i: 0 for i, _ in enumerate(interval_ranges)}

# Loop through each interval range and count the occurrences
for _, row in df.iterrows():
    val = row.iloc[0]
    for i, interval in enumerate(interval_ranges):
        start, end = interval
        if start <= val <= end:
            occurrences[i] += row.iloc[1]

# Create a new DataFrame to store the interval ranges and occurrence counts
interval_df = pd.DataFrame(interval_ranges, columns=['Start', 'End'])
interval_df[str(inputFilep1)+"_count"] = [occurrences[i] for i in range(len(interval_ranges))]

# Save the interval DataFrame to a new CSV file
interval_df.to_csv(str(inputFilep1) + '_interval_counts.csv', index=False)







# Read CSV file
df = pd.read_csv(outputFileForCO2)


# Determine the maximum value in column 1 and set that as the upper bound of the last interval range
max_val = df.iloc[:, 0].max()
interval_ranges =[]
startN = 0
endN = 100
difference = 100
while(True):
    interval_ranges.append((startN, endN))
    if (endN > max_val):
        break
    startN = endN + 1
    endN = endN + difference
    

# Initialize a dictionary to store the occurrence counts
occurrences = {i: 0 for i, _ in enumerate(interval_ranges)}

# Loop through each interval range and count the occurrences
for _, row in df.iterrows():
    val = row.iloc[0]
    for i, interval in enumerate(interval_ranges):
        start, end = interval
        if start <= val <= end:
            occurrences[i] += row.iloc[1]

# Create a new DataFrame to store the interval ranges and occurrence counts
interval_df = pd.DataFrame(interval_ranges, columns=['Start', 'End'])
interval_df[str(inputFilep2)+'_count'] = [occurrences[i] for i in range(len(interval_ranges))]

# Save the interval DataFrame to a new CSV file
interval_df.to_csv(str(inputFilep2) + '_interval_counts.csv', index=False)





filename = outputFileForCO1
col_num = 2
total1 = 0

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            total1 += float(row[col_num-1])  # Column indices start at 0
        except ValueError:
            pass  # Skip rows where column 2 is not a number





filename = outputFileForCO2
col_num = 2
total2 = 0

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            total2 += float(row[col_num-1])  # Column indices start at 0
        except ValueError:
            pass  # Skip rows where column 2 is not a number







input_filename = str(inputFilep1) + '_interval_counts.csv'
output_filename = str(inputFilep2) + '_interval_counts.csv'

# Read data from input file
with open(input_filename, 'r') as input_file:
    input_reader = csv.reader(input_file)
    input_data = list(input_reader)  # Convert iterator to list

# Read data from output file
with open(output_filename, 'r') as output_file:
    output_reader = csv.reader(output_file)
    output_data = list(output_reader)  # Convert iterator to list

# Determine which file has more rows
if len(input_data) > len(output_data):
    longer_data = input_data
    shorter_data = output_data
else:
    longer_data = output_data
    shorter_data = input_data
    temp = total2
    total2=total1
    total1 = temp

# Copy data from shorter file to longer file
for i, row in enumerate(shorter_data):
    if len(longer_data[i]) < 4:  # Check if row in longer file has a fourth column
        longer_data[i].append('')  # Add a new empty column if it doesn't
    longer_data[i][3] = row[2]  # Copy data from column 3 to column 4

# Write data to new output file
with open('Final_output.csv', 'w', newline='') as new_output_file:
    output_writer = csv.writer(new_output_file)
    output_writer.writerows(longer_data)




input_filename = 'Final_output.csv'

# Read data from input file
with open(input_filename, 'r') as input_file:
    input_reader = csv.reader(input_file)
    input_data = list(input_reader)
    input_data[0].insert(4, str(inputFilep1)+"_percentage")  # Add header to first row
    input_data[0].insert(5, str(inputFilep2)+"_percentage")  # Add header to first row


    # Calculate total and percentage for each row
    for row in input_data:
        try:
            column_3 = int(row[2]) if len(row) > 2 and row[2] else 0
            column_4 = int(row[3]) if len(row) > 3 and row[3] else 0
            percentage3 = (column_3 / total1) * 100  # Assuming total is calculated before
            percentage4 = (column_4 / total2) * 100
            # print(row[3])
            if len(row) < 4:
                row.append(0)
                row.append(str(percentage3))
                row.append(str(percentage4))
            else:
                row.append(str(percentage3))  # Add percentage as a new column
                row.append(str(percentage4))
        except ValueError:
            pass  # Skip row if column 3 or 4 is not a valid integer


    # Compute column totals
    col3_total = sum(float(row[2]) for row in input_data[1:])
    col4_total = sum(float(row[3]) for row in input_data[1:])
    col5_total = sum(float(row[4]) for row in input_data[1:])
    col6_total = sum(float(row[5]) for row in input_data[1:])

    # Create output row with column totals
    output_row = ['', '', f'Total {col3_total:.2f}', f'Total {col4_total:.2f}', f'Total {col5_total:.2f}', f'Total {col6_total:.2f}']



# Write updated data to the output file
with open('Final_output.csv', 'w', newline='') as output_file:
    output_writer = csv.writer(output_file)
    output_writer.writerows(input_data)
    output_writer.writerow(output_row)  # Write output row





# Define lists to hold the x and y values
x_values = []
y_values1 = []
y_values2 = []

# Read the CSV file
with open('Final_output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # Skip the header row
            line_count += 1
        elif len(row) != 6:
            # Skip rows that do not have 7 columns
            continue
        else:
            
            # Try to convert data in column 5 and 6 to float with 2 decimal places
            try:
                x = float("{:.2f}".format(float(row[1])))
                y1 = float("{:.2f}".format(float(row[4])))
                y2 = float("{:.2f}".format(float(row[5])))
                x_values.append(x)
                y_values1.append(y1)
                y_values2.append(y2)
            except ValueError:
                # Skip rows where either column 5 or 6 does not contain numeric data
                continue
                
            line_count += 1


# print(x_values)
# print(y_values1)
# print(y_values2)

# Plot the data
plt.plot(x_values[:len(y_values1)], y_values1, color='blue')
plt.plot(x_values[:len(y_values2)], y_values2, color='red')

# Add labels and title
plt.xlabel('Range')
plt.ylabel('Number of Protein')
plt.title('Graph of Data from CSV File')
plt.xticks(np.arange(0, 1900, 400))

# Display the plot
plt.show()