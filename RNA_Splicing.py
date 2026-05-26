introns=[]
start=0
dna_seq=""

with open("r.txt") as f:
    lines = [line.strip() for line in f]

i = 0

i += 1
while i < len(lines) and not lines[i].startswith(">"):
    dna_seq += lines[i]
    i += 1

while i < len(lines):
    if lines[i].startswith(">"):
        intron = ""
        i += 1

        while i < len(lines) and not lines[i].startswith(">"):
            intron += lines[i]
            i += 1

        introns.append(intron)
       
for i in introns:
    dna_seq=dna_seq.replace(i,"")

start = dna_seq.find("ATG")
dna_seq = dna_seq[start:]

genetic_code = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

   
def translate_dna(dna_seq):
    protein_seq = ""
    for i in range(0, len(dna_seq)-2, 3):
        codon = dna_seq[i:i+3]
        amino_acid = genetic_code.get(codon.upper(), 'X') 
        if amino_acid == '*':
            break 
        protein_seq += amino_acid
    return protein_seq


protein_sequence = translate_dna(dna_seq)
print("protein sequence: ",protein_sequence)