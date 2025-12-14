def gc_content(dna):
    return 100 * (dna.count('G') + dna.count('C')) / len(dna)

fasta_input = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

max_id = ""
max_gc = 0.0

current_id = ""
current_seq = ""

for line in fasta_input.strip().splitlines():
    line = line.strip()
    if line.startswith(">"):
        if current_seq:
            gc = gc_content(current_seq)
            if gc > max_gc:
                max_gc = gc
                max_id = current_id
        current_id = line[1:]
        current_seq = ""
    else:
        current_seq += line

gc = gc_content(current_seq)
if gc > max_gc:
    max_gc = gc
    max_id = current_id

print(max_id)
print(f"{max_gc:.6f}")
