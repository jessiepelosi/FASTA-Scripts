# FASTA Scripts and Tools 

This is a repository of code for basic work with FASTA files.  

Current contents include:

- get_read_length.py  
- replace_headers.py


# get_read_length.py
This script is used to extract the length of each read/contig/scaffold in a given FASTA file. 
Input: FASTA file
Output: two column .txt, first column is the header name, second column is the length of the corresponding read/contig/scaffold 
Usage: 
<tt> get_read_length.py [input_fasta] <\tt>
  
# replace_headers.py
This script is used to replace headers in a FASTA based on a matching string.
Input: FASTA file
Output: FASTA file with replaced headers, named your_fasta_fixed
Usage:
<tt> replace_headers.py [input_fasta] <\tt> 
  
  
Last modified 20 May, 2020 
