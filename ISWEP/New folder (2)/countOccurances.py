import csv
def countOccurances(csvFile, outputCSVFile):
    # Open the CSV file
    with open(csvFile, 'r') as csv_file:

        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)

        # Skip the header row
        next(csv_reader)

        # Create an empty dictionary to store the counts
        counts = {}

        # Loop through each row in the CSV file
        for row in csv_reader:
            
            # Extract the number from the 3rd column
            num = row[1]

            # Update the count for the number in the dictionary
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

    # Create a new CSV file to store the counts
    with open(outputCSVFile, 'w', newline='') as csv_file:

        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(['Number', 'Occurrences'])

        # Write each row to the CSV file
        for num, count in counts.items():
            csv_writer.writerow([num, count])
if __name__=="__main__":
    csvFile = 'proteins.csv'
    outputCSVFile = 'count.csv'
    countOccurances(csvFile, outputCSVFile)