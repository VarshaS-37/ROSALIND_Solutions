s=input('enter first seq:').upper()
t=input('enter second seq:').upper()
dis=0
for i in range(len(s)):
    if s[i]!=t[i]:
        dis=dis+1 
print(f'Hamming distance is {dis}')