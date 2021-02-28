def adigits(n1, n2, n3):
    digits = [n1, n2, n3]
    digits.sort(reverse=True)
    
    result = 0
    for i in digits:
        result *= 10
        result += i

    return result
