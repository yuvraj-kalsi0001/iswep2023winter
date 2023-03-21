# Open the input GFF file and output files
with open('albidoflavus_J1074.gff', 'r') as infile, open('output1.gff', 'w') as outfile1, open('output2.gff', 'w') as outfile2:

    # Initialize variables to keep track of the previous chromosome and gene ID
    prev_chromosome = ''
    prev_gene_id = ''

    # Loop through each line of the input file
    for line in infile:

        # Skip comment lines
        if line.startswith('#'):
            continue

        # Split the line into fields
        fields = line.strip().split('\t')

        # Extract the chromosome, gene ID, and locus tag
        chromosome = fields[0]
        gene_id = fields[4]
        locus_tag = fields[6]

        # If the chromosome or gene ID has changed, write to the appropriate output file
        if chromosome != prev_chromosome or gene_id != prev_gene_id:
            if chromosome != prev_chromosome:
                outfile1.write('\n')  # Add a blank line to separate chromosomes
            outfile1.write(line)
            prev_chromosome = chromosome
            prev_gene_id = gene_id
        else:
            outfile2.write(line)

# Close the input and output files
infile.close()
outfile1.close()
outfile2.close()
