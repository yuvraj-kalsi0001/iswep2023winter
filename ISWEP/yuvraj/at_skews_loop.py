import os
import matplotlib.pyplot as plt
from Bio import SeqIO

# Create a list of all fasta files in the directory
directory = "/home/streptomyces/Menus/at_skew_python_8_script"
fasta_files = [f for f in os.listdir(directory) if f.endswith('.fasta')]

# Loop through each fasta file
for fasta_file in fasta_files:
    a_count = 0
    t_count = 0
    g_count = 0
    c_count = 0
    at_skews = []
    cum_at_skews = []
    cum_at_skew = 0
    window = 5000
    i = 0
    # Parse the fasta file using Bio.SeqIO
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = record.seq
        # Count the number of A, T, G, and C in the sequence
        for base in seq:
            if base == 'A':
                a_count += 1
            elif base == 'T':
                t_count += 1
            elif base == 'G':
                g_count += 1
            elif base == 'C':
                c_count += 1
            i += 1
            if i % window == 0:
                at_skew = (a_count - t_count) / (a_count + t_count)
                at_skews.append(at_skew)
                cum_at_skew += at_skew
                cum_at_skews.append(cum_at_skew)
                a_count = 0
                t_count = 0
                g_count = 0
                c_count = 0
    # Plot the AT skew and cumulative AT skew in the same graph
    plt.figure()
    ax1 = plt.subplot(111)
    ax1.plot(at_skews, label='AT skew')
    ax1.plot(cum_at_skews, label='Cumulative AT skew')
    plt.legend()
    plt.xlabel('Window')
    plt.ylabel('Skew')
    plt.title(fasta_file + ' AT skew')
    # Save the graph with the same name as the fasta file
    plt.savefig(fasta_file + '.png')
