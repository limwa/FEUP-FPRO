n = int(input())

result = "1"
for i in range(2, n + 1):
    if i % 3 == 0 and not i % 5 == 0:
        result += " Fizz"
    elif i % 5 == 0 and not i % 3 == 0:
        result += " Buzz"
    elif not i % 3 == 0 and not i % 5 == 0:
        result += " " + str(i)
        
print(result)
