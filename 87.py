# 87
a = int(input("how many numbers you want to enter: "))
b = []

for i in range(a):

    b.append(int(input()))


b.sort(reverse=True)

print(b)