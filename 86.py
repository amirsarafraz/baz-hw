# 86
def k():
    a = int(input( "how many number you want to enter: "))
    b = []
    for i in range(a):
        b.append(int(input()))

    max = b[0]

    for i in b:
        if i > max:
            max = i
    return max

print(k())