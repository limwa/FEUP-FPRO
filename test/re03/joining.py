# This was the only exercises where I got a grade lower than 100%
# This algorithm failed for the private test    '56', '0' --> '560'

first, second = int(input()), int(input())

copy = second
length = 0
while copy >= 1:
    length += 1
    copy /= 10

print(first * 10 ** length + second)
