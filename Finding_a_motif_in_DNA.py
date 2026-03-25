sequence=input("Enter DNA sequence ")
motif=input("Enter the motif to be found ")
found_motifs=[]
for i in range(0,len(sequence)-len(motif)+1):
    if (sequence[i:i+len(motif)] == motif):
        found_motifs.append(i+1)
print("The starting positions of the given motif in the DNA sequence are: ",*found_motifs)