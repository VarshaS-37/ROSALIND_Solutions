no=int(input("Enter n: "))
no=no-1
nos_list=[]

for i in range(1,no+2):
    nos_list.append(str(i))

perms=[]

def perm(c):

    if len(c) == no+1:
        perms.append(c)
        return

    for i in nos_list:
        if i not in c:
          perm(str(c) + i)
   
perm("")
print(len(perms))
for i in perms:
    nos=list(i)
    for digit in nos:
        print(int(digit), end=" ")
    print("")




