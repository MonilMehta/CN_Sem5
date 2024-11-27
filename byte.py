mes=input('Enter the message: ')
flag=input('Enter the flag: ')
esc=input('Enter the escape character: ')

if(mes.find(flag)!=-1 or mes.find(esc)!=-1):
    i=mes.find(esc)
    while i!=-1:
        mes=mes[:i]+esc+mes[i:]
        i=mes.find(esc,i+2)
    i=mes.find(flag)
    while i!=-1:
        mes=mes[:i]+esc+mes[i:]
        i=mes.find(flag,i+2)

print(flag+mes+flag)

message=flag+mes+flag

i=1
print('Message : ')
while i<len(message)-1:
    if message[i]==esc:
        print(message[i+1],end='')
        i+=2
    else:
        print(message[i],end='')
        i+=1