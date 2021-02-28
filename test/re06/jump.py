def jump(l):
    result = 0

    i = 0
    while i != -1:
        i = l[i]
        result += 1

    return result - 1
