def order_digits(n):
    return tuple(sorted([int(i) for i in list(str(n))], reverse=True))
