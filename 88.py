a = int(input( "how many number you want to enter: "))
arr1 = []
arrcheck=[]

for i in range(a):
    x=(int(input()))
    arr1.append(x)
    arrcheck.append(x)
arrcheck.sort(reverse=False)

# print(arrcheck)
for m in range(len(arr1)):
    
    if arrcheck[m]==arr1[m]:
        print("True")
        break
    else:
        print("False")
        break

