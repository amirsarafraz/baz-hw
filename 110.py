

def numsort():
    a = int(input())
    num = []



    for i in range(a):
        number = int(input())
        
        num.append(number)

    num.sort(reverse=True)
    return num

print(numsort())