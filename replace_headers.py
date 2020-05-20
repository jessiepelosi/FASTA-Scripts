'''
Purpose: replace FASTA headers in cds alignments with taxon names for input into codeml and alignemnt with trees used

Usage: python replace_headers.py input_fasta
Arguments: 
	Input_fasta: aligned cds fasta file to change headers 

last modified 20 May 2020 
'''

from Bio import SeqIO
import sys 
args = sys.argv 
input_txt = sys.argv[1]


with open(input_txt) as infile, open(input_txt + "fixed", 'w') as corrected:
	records = SeqIO.parse(infile, 'fasta')
	for record in records:
		if "Adiantum_tenerum" in record.id: #replace this with what the header currently is 
		# or, more importantly, if this is in any part of the header, you'll replace it with 
		# what is in the next line  
			record.id = "Adiantum_raddianum" #replace this with what you want the header to be 
			# i.e., I want the header to be >Adiantum_raddianum
			record.description = "Adiantum_raddianum" # replace this as well, sometimes 
			# description is actually the thing you want to change so include both of these 
		elif "Vittaria_appalachiana" in record.id: # Add or removed elif statements for 
		#depending on the number of headers you want to replace 
			record.id = "Vittaria_appalachiana"
			record.description = "Vittaria_appalachiana"
		elif "Vittaria_lineata" in record.id:
			record.id = "Vittaria_lineata"
			record.description = "Vittaria_lineata" 
		SeqIO.write(record, corrected, 'fasta')
