dna_seq=input('Enter DNA sequence:').upper()
dna_seq_rev=dna_seq[::-1]
compl=""
for nuc in dna_seq_rev:
    if nuc=="A":
        compl+="T"
    if nuc=="C":
        compl+="G"
    if nuc=="G":
        compl+="C"
    if nuc=="T":
        compl+="A"
print(compl)
