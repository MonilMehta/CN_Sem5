deg=int(input("Enter degree: "))
poly=[]
for i in range(deg+1):
    poly.append(int(input(f"Enter coefficient of x^{deg-i}: ")))

og=int(input("Enter length of original data: "))
data=[]
for i in range(og):
    data.append(int(input(f"Enter data bit {i+1}: ")))

data_copy=data.copy()
remainder=data[:deg+1]

data.extend([0]*deg)

for i in range(og):
    if remainder[0]==1:
        for j in range(deg+1):
            remainder[j]^=poly[j]
    remainder.pop(0)
    if i+deg+1<len(data):
        remainder.append(data[i+deg+1])

codeword=data_copy+remainder
print(f"Codeword: {codeword}")

print("Decoding : ")
data=[1,0,1,1,1,0,1]
remainder=data[:deg+1]


for i in range(og):
    if remainder[0]==1:
        for j in range(deg+1):
            remainder[j]^=poly[j]
    remainder.pop(0)
    if i+deg+1<len(data):
        remainder.append(data[i+deg+1])

if sum(remainder)==0:
    print("No error detected")
else:
    print("Error detected")