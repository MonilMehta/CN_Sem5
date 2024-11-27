mes=input('Enter the message: ')
c=0

stuffed=''

for i in mes:
    if i=='1':
        c+=1
        stuffed+=i
    else:
        c=0
        stuffed+=i
    if c==5:
        stuffed+='0'
        c=0

print(stuffed)

print('Decode:')

c=0
for i in stuffed:
    if i=='1':
        c+=1
        print(i,end='')
    else:
        c=0
        print(i,end='')
    if c==5:
        c=0
        continue
