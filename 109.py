def faktorial():
    n = int(input())

    for i in range(n):
        number = int(input())
        result = 1
        for j in range(1, number+1):
            result *= j
        print(f"{number} != {result}")


faktorial()