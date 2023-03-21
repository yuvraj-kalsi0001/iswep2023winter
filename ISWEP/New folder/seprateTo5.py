import csv
import gffutils

def createFiveFiles():
    # Open the input CSV file and create a CSV reader object
    with open('gene_presence_absence.csv', 'r') as input_file:
        reader = csv.reader(input_file)

        # Create a dictionary to hold the output files
        output_files = {}

        # Loop over each row in the input CSV file
        for row in reader:
            # Get the value in column 5 (assuming columns are 0-indexed)
            col_5_value = row[4]

            # If this is the first row or if the value in column 5 has changed
            if not output_files or col_5_value not in output_files:
                # Create a new output file for this value in column 5
                output_filename = f'{col_5_value}.csv'
                output_files[col_5_value] = open(
                    output_filename, 'w', newline='')
                output_writer = csv.writer(output_files[col_5_value])

            # Write the current row to the appropriate output file
            output_writer.writerow(row)

        # Close all of the output files
        for output_file in output_files.values():
            output_file.close()
    # import csv

    # # Open the input CSV file and create a CSV reader object
    # with open('gene_presence_absence.csv', 'r') as input_file:
    #     reader = csv.reader(input_file)

    #     # Create a dictionary to hold the output files
    #     output_files = {}

    #     # Loop over each row in the input CSV file
    #     for i, row in enumerate(reader):
    #         # Get the value in column 5 (assuming columns are 0-indexed)
    #         col_5_value = row[4]

    #         # If this is the first row or if the value in column 5 has changed
    #         if not output_files or col_5_value not in output_files:
    #             # Create a new output file for this value in column 5
    #             output_filename = f'{col_5_value}.csv'
    #             output_files[col_5_value] = open(output_filename, 'w', newline='')
    #             output_writer = csv.writer(output_files[col_5_value])

    #             # If this is not the first row, write the first row to the new file
    #             if i > 0:
    #                 input_file.seek(0)
    #                 first_row = next(reader)
    #                 output_writer.writerow(first_row)

    #         # Write the current row to the appropriate output file
    #         output_writer.writerow(row)

    #     # Close all of the output files
    #     for output_file in output_files.values():
    #         output_file.close()



def createNewFile():
    

    # Step 1: Read in the data from the first CSV file and store it as a set
    data_set = set()
    with open('5.csv', 'r') as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            data_set.add(tuple(row[i] for i in range(15)))

    # Step 2: Connect to the GFF file and loop over the features
    matches = []
    db = gffutils.create_db('albidoflavus_J1074.gff', ':memory:', merge_strategy='merge')
    for feature in db.features_of_type(''):
        attributes = feature.attributes
        if tuple(attributes[attr] for attr in range(9)) in data_set:
            matches.append(attributes)

    # Step 3: Write the matching attributes to a new CSV file
    with open('output.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(matches)





def main():
    createFiveFiles()
    # createNewFile()


main()
