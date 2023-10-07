m=[]
for i in range(10):

    a=int(input())
    if a%2==0 or a%3==0:
        if a!=3:
            m.append(a)

print(m)