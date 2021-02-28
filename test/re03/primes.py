num = int(input())
print(len([i for i in range(1, num + 1) if num % i == 0]) == 2)
