import csv
import sys

def cropFile(filename):

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
        nextFiles = []

        # Create separate output files for columns 1 and 15 onwards
        output_files = {}
        for i in range(14, len(header)):
            # if i == 15:
            #     break
            output_files[i] = open(f'' + header[i] + '.csv', 'w', newline='')
            writer = csv.writer(output_files[i])
            writer.writerow(['Gene', header[i]])
            nextFiles.append(header[i])

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

    return nextFiles


def extendExcel(file):
    # read column 2 from csv file
    csv_col2 = set()
    with open(file + '.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip header
        for row in csv_reader:
            csv_col2.add(row[1])

    # read column 9 from gff file
    gff_col9_to_col7 = {}
    with open(file + '.gff', 'r') as gff_file:
        for line in gff_file:
            if line.startswith("##FASTA"): break
            if not line.startswith('#'):
                line_data = line.split('\t')
                col9 = line_data[8].split(';')[0].split('=')[1]
                col7 = line_data[6]
                col4 = line_data[3]
                col5 = line_data[4]
                gff_col9_to_col7[col9] = [col4, col5, col7]

    # update column 3 in csv file
    with open(file + '.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # get header
        header.append('Sign')  # add new column
        header.append('Start')  # add new column
        header.append('End')  # add new column
        rows = []
        for row in csv_reader:
            if row[1] in gff_col9_to_col7:
                row.append(gff_col9_to_col7[row[1]][2])
                row.append(gff_col9_to_col7[row[1]][0])
                row.append(gff_col9_to_col7[row[1]][1])
            else:
                row.append('')
            rows.append(row)

    # write updated data to csv file
    with open(file + '.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        csv_writer.writerows(rows)


def main():
    # "gene_presence_absence.csv"
    gene_presence_absence = sys.argv[1]
    cropFile(gene_presence_absence)
    nextFilesToProcess = makeCombination('output.csv')
    for i in nextFilesToProcess:
        extendExcel(i)

main()

