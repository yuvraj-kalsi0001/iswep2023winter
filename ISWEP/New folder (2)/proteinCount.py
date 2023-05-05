import csv
def proteinCount(fastaFile, csvFile):

    # Open the input FASTA file for reading
    with open(fastaFile, 'r') as f:

        # Open the output CSV file for writing
        with open(csvFile, 'w', newline='') as g:

            # Create a CSV writer object
            writer = csv.writer(g)
            writer.writerow(["protein_number", "protein_name", "length of protein_seq"])

            # Initialize the protein counter
            protein_count = 0

            # Initialize the protein name and sequence strings
            protein_info = ''
            protein_seq = ''

            # Loop through each line in the FASTA file
            for line in f:

                # Check if this line is the start of a new protein
                if line.startswith('>'):
                    # If so, increment the protein counter and write the data to the CSV file
                    if protein_count > 0:
                        writer.writerow([protein_info, len(protein_seq)])
                    protein_count += 1
                    protein_info = line.strip()[1:]
                    # print(protein_name)
                    protein_seq = ''
                else:
                    # Otherwise, add the line to the protein sequence string
                    protein_seq += line.strip()

            # Write the final protein to the CSV file
            writer.writerow([protein_info, len(protein_seq)])


    # Set the file paths
    input_file = csvFile
    output_file = csvFile

    # print(csvFile)

    # Read the input CSV file
    data = []
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        # Skip the header row
        next(reader)
        # Read the remaining rows
        for row in reader:
            data.append(row)

    # Sort the data based on the third column
    data.sort(key=lambda x: int(x[1]))

    # Write the sorted data to the output CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        # Write the header row
        writer.writerow(["protein_info","length of protein_seq"])
        # Write the sorted rows
        for row in data:
            writer.writerow(row)

if __name__=="__main__":
        
    # Set the file paths
    fasta_file = '11-1-2.faa'
    csv_file = 'proteins.csv'
    proteinCount(fasta_file,csv_file)




