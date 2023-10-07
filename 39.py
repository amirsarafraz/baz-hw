#39
def bainary ():
    a=input()
    h = ' '
    if len(a)==4:
        for n in a:
            if n=='1':
                h+=n
    return h

print(bainary())