#37
def sort ():
    a=int(input())
    b=int(input())
    c=int(input())
    if a>b and b>c:
        return a,b,c
    if a>c and c>b:
        return a,c,b
    elif b>a and a>c:
        return b,a,c
    elif b>a and a<c:
        return b,c,a
    elif c>a and a>b:
        return c,a,b
    elif c>a and a<b:
        return c,b,a
    
print(sort())