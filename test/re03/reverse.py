num = int(input())

result = 0

while num > 0:
    digit = num % 10
    num //= 10

    result = result * 10 + digit

print(result)
