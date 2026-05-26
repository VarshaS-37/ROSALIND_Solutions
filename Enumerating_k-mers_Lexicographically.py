alphabets=list(map(str, input("Enter symbols: ").split()))
no=int(input("Enter n: "))

combos=[]

def combo(p):

    if len(p) == no:
        combos.append(p)
        return

    for i in range(len(alphabets)):
        combo(p + alphabets[i])
   
combo("")

for i in combos:
    print(i)