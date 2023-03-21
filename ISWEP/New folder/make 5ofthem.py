import csv
import gffutils

def makeFiveFiles(filename):

    # Open input file
    with open(filename, 'r') as input_file:
        reader = csv.reader(input_file)
        
        # Read header and first row
        header = next(reader)
        first_row = next(reader)
        previous_value = first_row[4]  # assuming column 5 is the one to check
        
        # Create output file
        output_filename = "output.csv"
        with open(output_filename, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)
            writer.writerow(first_row)
            output_row = [header[i] for i in range(len(header))]  # copy header row
            
            # Copy data until value in column 5 changes
            for row in reader:
                if row[4] != previous_value:
                    break
                writer.writerow(row)
                output_row.append(row[i] for i in range(len(row)))  # copy data row
            
            print(f"Copied {len(output_row)} rows to {output_filename}")


def makeCombination(fileName):
    # Open the input CSV file
    with open(fileName, 'r') as input_file:
        # Create a CSV reader object
        reader = csv.reader(input_file)

        # Read the header row
        header = next(reader)

        # Create separate output files for columns 1 and 15 onwards
        output_files = {}
        for i in range(14, len(header)):
            # if i == 15:
            #     break
            output_files[i] = open(f'column_' + header[i] + '.csv', 'w', newline='')
            writer = csv.writer(output_files[i])
            writer.writerow(['Gene', header[i]])

        # Copy the data rows and columns to the appropriate output files
        for row in reader:
            for i in range(14, len(row)):
                # if i == 15:
                #     break
                writer = csv.writer(output_files[i])
                writer.writerow([row[0], row[i]])

    # Close all output files
    for file in output_files.values():
        file.close()


def extendExcel():
    # Open the CSV file and read data from column 2
    with open('column_albidoflavus_J1074.csv', 'r') as file1:
        reader1 = csv.reader(file1)
        next(reader1)  # Skip header row
        column2_data = [row[1] for row in reader1]

    # Open the GFF file and read data from column 9 and column 7
    with open('albidoflavus_J1074.gff', 'r') as file2:
        column9_data = []
        column7_data = []
        for line in file2:
            # print(line)
            if line.startswith("##FASTA"): break
            if not line.startswith('#'):
                data = line.strip().split('\t')
                column9_data.append(data[8])
                column7_data.append(data[6])
    
    # print(column2_data)
            
                

    # Loop through the column 2 data and search for matches in column 9 data
    for i, value in enumerate(column2_data):
        for gene in range(len(column9_data)):
            if value in column9_data[gene]:
                # If a match is found, copy the corresponding data from column 7 to column 3 of the CSV file
                # with open('column_albidoflavus_J1074.csv', 'r') as file1, open('new_column_albidoflavus_J1074.csv', 'w', newline='') as output:
                #     reader1 = csv.reader(file1)
                #     writer = csv.writer(output)
                #     for j, row in enumerate(reader1):
                #         if j == 0:
                #             # Write the header row
                #             writer.writerow(row + ['Column 3'])
                #         else:
                #             if row[1] == value:
                #                 # If the value from column 2 matches, copy data from column 7 to column 3
                #                 writer.writerow(row + [column7_data[column9_data.index(value)]])
                #                 print(column7_data[column9_data.index(value)])
                #             else:
                #                 writer.writerow(row)

                # Open GFF file
                # print("true")


                # with open('albidoflavus_J1074.gff', 'r') as file1, open('column_albidoflavus_J1074.csv', 'w', newline='') as output:
                #     reader1 = csv.reader(file1, delimiter='\t')  # Set delimiter to tab
                #     writer = csv.writer(output)

                #     for j, row in enumerate(reader1):
                #         if row[0].startswith('#'):
                #             continue  # Skip comment lines

                #         if j == 0:
                #             # Write the header row
                #             writer.writerow(row + ['Column 3'])
                #         else:
                #             value = row[1]
                #             # Extract column 7 data
                #             column7_data = row[8].split(';')
                #             column7_data = [d.split('=')[1] for d in column7_data if d.startswith('ID=')]

                #             if value in column7_data:
                #                 # If the value from column 2 matches, copy data from column 7 to column 3
                #                 writer.writerow(row + [value])
                #                 print(value)
                #             else:
                #                 writer.writerow(row)



                

                db = gffutils.create_db('column_albidoflavus_J1074.gff', dbfn='column_albidoflavus_J1074.db', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)

                with open('column_albidoflavus_J1074.gff', 'w') as output:
                    for i, feature in enumerate(db.all_features()):
                        if i == 0:
                            # Write the header row
                            output.write('\t'.join(feature.attributes.keys()) + '\t' + 'Column 3\n')
                        else:
                            if feature.attributes['attribute2'][0] == value:
                                # If the value from attribute2 matches, copy data from attribute7 to column 3
                                output.write('\t'.join(feature.attributes.values()) + '\t' + feature.attributes['attribute7'][0] + '\n')
                                print(feature.attributes['attribute7'][0])
                            else:
                                output.write('\t'.join(feature.attributes.values()) + '\n')








def main():
    # makeFiveFiles("gene_presence_absence.csv")
    # makeCombination('output.csv')
    extendExcel()

main()

