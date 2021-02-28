def get_neighbors(l, radius, i):
    start = max(i - radius, 0)
    end = min(i + radius + 1, len(l))
    return l[start:i] + l[(i + 1):end]

def local_minima(alist, n):
    radius = (n - 1) // 2

    result = []
    for i in range(len(alist)):
        neighbors = get_neighbors(alist, radius, i)
        el = alist[i]

        is_minimum = True
        for neighbor in neighbors:
            if not el <= neighbor:
                is_minimum = False
                break

        if is_minimum:
            pair = (el, i)
            if len(result) > 0:
                minimum, index = result[len(result) - 1]
                if abs(index - i) > radius:
                    result.append(pair)
            else:
                result.append(pair)

    return result
