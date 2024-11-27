# d7 d6 d5 p4 d3 p2 p1

d7=int(input("Enter d7: "))
d6=int(input("Enter d6: "))
d5=int(input("Enter d5: "))
d3=int(input("Enter d3: "))
parity=input("Enter parity: ")

if parity==1:
    p1=(d7+d5+d3+1)%2
    p2=(d7+d6+d3+1)%2
    p4=(d7+d6+d5+1)%2
else:
    p1=(d7+d5+d3)%2
    p2=(d7+d6+d3)%2
    p4=(d7+d6+d5)%2

print(d7,d6,d5,p4,d3,p2,p1)

print("Enter code: ")
d7=int(input())
d6=int(input())
d5=int(input())
p4=int(input())
d3=int(input())
p2=int(input())
p1=int(input())

if parity==1:
    p11=(d7+d5+d3+p1)%2
    p22=(d7+d6+d3+p2)%2
    p44=(d7+d6+d5+p4)%2
else:
    p11=(d7+d5+d3+p1+1)%2
    p22=(d7+d6+d3+p2+1)%2
    p44=(d7+d6+d5+p4+1)%2

if p1==p11 and p2==p22 and p4==p44:
    print("No error")
else:
    error=p1+p2*2+p4*4
    print("Error at position: ",error)
    print("Corrected code: ")
    