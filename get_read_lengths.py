'''
Purpose: produce a list of lengths for each contig or read from a fasta input file
Usage:
	python get_read_lengths.py [input file.fasta] [output file.txt]
Arugments: 
	input file: fasta-format file, from which to extract length of each read or contig (>)
	output file: text file that will contain one column of headers and one column of lengths 

Last modified April 17, 2020 
Jessie Pelosi 

'''

import sys 
args = sys.argv 
input_fasta = sys.argv[1]
output_file = sys.argv[2]

input_file = open(input_fasta, 'r')
output = open(output_file, "w+")
output.write('Read\tLength\n')

from Bio import SeqIO

for cur_record in SeqIO.parse(input_file, "fasta"):
	contig_name = cur_record.name
	length = len(cur_record.seq)
	output_line = '%s\t%i\n' % \
	(contig_name, length)
	output.write(output_line) 

input_file.close()
output.close()

