ip=input("Enter ip address:")

ip=ip.split(".")

if len(ip)!=4:
    print("Invalid IP")

else:
    first=int(ip[0])
    if first>=0 and first<=127:
        print("Class: A")
        print("Subnet mask: 255.0.0.0")
        ip[1]=ip[2]=ip[3]="0"
        subnet=".".join(ip)
        print("Subnet address: ",subnet)
    if first>=128 and first<=191:
        print("Class: B")
        print("Subnet mask: 255.255.0.0")
        ip[2]=ip[3]="0"
        subnet=".".join(ip)
        print("Subnet address: ",subnet)
    if first>=192 and first<=223:
        print("Class: C")
        print("Subnet mask: 255.255.255.0")
        ip[3]="0"
        subnet=".".join(ip)
        print("Subnet address: ",subnet)
    if first>=224 and first<=239:
        print("Class: D")
        print("Multicast")
    if first>=240 and first<=255:
        print("Class: E")
        print("Reserved")