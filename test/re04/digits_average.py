import math

def digits_average(n):
    while n > 9:
        copy = n
        n = 0
        
        for i in range(1, length(copy)):
            average = math.ceil((get_digit(copy, i) + get_digit(copy, i - 1)) / 2)
            n = concatenate(average, n) if n != 0 else average

    return n

def get_digit(n, i):
    mult = 10 ** i
    return (n // mult) % 10

def concatenate(n, n1):
    return n * 10 ** length(n1) + n1

def length(n):
    return 1 if n == 0 else int(math.log(n, 10)) + 1
