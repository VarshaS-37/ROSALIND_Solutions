dna_in=[]
print("enter the dna sequence and press enter twice after entering the sequence:")
while True:
    line=str(input())
    if line=="":
        break
    dna_in.append(line)
dna="".join(dna_in)
length=range(4,12)
complements={'A':'T','G':'C',"T":"A","C":"G"}
palindrome_pairs=[]
for j in range(3,12):
    for i in range(0,len(dna)-j):
        substring=dna[i:i+j+1]
        reverse_complement=""
        for nucleotide in substring.upper():
            reverse_complement+=complements[nucleotide]
        reverse_complement=reverse_complement[::-1]
        if substring.upper()==reverse_complement:
            palindrome_pairs.append((i+1,len(reverse_complement)))
            print(f"The reverse palindrome is {substring.upper()} at position {i+1} with length {len(reverse_complement)}")
print(f"The reverse palindrome position and length pairs are:")
for pair in palindrome_pairs:
    print(*pair,sep="\t")
    