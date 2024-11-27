n=int(input("Enter no of messaages : "))

li=[]

for i in range(n):
    li.append(input("Enter message : "))

mes=''
for i in li:
    mes+=str(len(i)+1)
    mes+=i

print(mes)

i=0
while i<len(mes):
    if mes[i].isnumeric():
        n=int(mes[i])
        print(mes[i+1:i+n],end=' ')
        i+=n
    else:
        print(' ',end='')