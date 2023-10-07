num = input()

for digit in num:
    n = ord(digit)
    if 48 <= n <= 57:
        
        print(n - 48)