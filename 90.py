n = int(input())

for i in range(n):



    num = int(input())
    res = 1

    
    for j in range(1, num+1):
        res *= j
    print(f"{num} != {res}")