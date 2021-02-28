num = int(input())

x = num / 2
prev_x = -1

while True:
    prev_x = x
    x = (prev_x + num / prev_x) / 2

    if round(x - prev_x, 2) == 0:
        break

print(round(x, 2))
