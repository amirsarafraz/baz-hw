def a():
    m=[]
    sum=0
    for i in range(5):
        x=(int(input()))
        m.append(x)
        sum+=x
    sum=sum/5
    for i in m:
        if i-sum>=3:
            print(i)

a()

    