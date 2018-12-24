from Bio import SeqIO

# fasta_data = SeqIO.parse("dna.example.fasta", "fasta")
fasta_data = SeqIO.parse("dna2.fasta", "fasta")

#for record in fasta_data:
    #print(record)

records = list(fasta_data)

print(len(records))
#print(records[0])
#print(dir(records[1]))

max = len(records[0].seq)
min = len(records[0].seq)

#Track Longest and Shortest
for record in records:
    record_len = len(record.seq)
    if record_len > max:
        max=record_len
    elif record_len < min:
        min=record_len

print(max)
print(min)
