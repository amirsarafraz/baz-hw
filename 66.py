
n = []
for i in range(100):
    num = int(input())
    n.append(num)
    
f1 = 0
f2 = 1
count = 0

for i in num:
    if i % 2 == 1:
        while f2 < i:
            fsum = f1 + f2
            f1 = f2
            f2 = fsum
        if f2 == i:
            count += 1

print(count)
    
        

