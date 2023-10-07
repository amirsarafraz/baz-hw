# a=int(input())
    
# f1 = 0
# f2 = 1
# count = 0

# for i in range(len(a)):
    
#     # while f2 < i:
#     fsum = f1 + f2
#     f1 = f2
#     f2 = fsum
#     if f2 %a== 0:
#         print(f2)
# a=int(input())

# f1 = 0
# f2 = 1
# count = 0

# for i in range(a):
    
#     fsum = f1 + f2
#     f1 = f2
#     f2 = fsum
#     if f2 %a== 0 and f2<100000:
#         print(f2)

a = int(input())

f1 = 0
f2 = 1

count = 0


while f2 <= 100000:
    if f2 % a == 0:
        print(f2)
    fsum = f1 + f2
    f1 = f2
    f2 = fsum
