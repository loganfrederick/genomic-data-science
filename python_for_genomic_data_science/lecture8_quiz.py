from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

fasta_string="TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG"
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
blast_record = NCBIXML.read(result_handle)

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        print('****Alignment****')
        print('sequence:', alignment.title)
        print('length:', alignment.length)
        print('e value:', hsp.expect)
        print(hsp.query)
        print(hsp.match)
        print(hsp.sbjct)
