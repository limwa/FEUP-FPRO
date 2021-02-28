def is_good(M):
    width = len(M[0])
    for row in M:
        if len(row) != width:
            return False
    return True

def is_possible(M, N):
    if not is_good(M) or not is_good(N):
        return False

    return len(M[0]) == len(N)

def get_dims(M, N):
    # (width, height)
    return (len(N[0]), len(M))

def get_element_at(M, N, i, j):
    result = 0
    for index in range(len(N)):
        result += M[j][index] * N[index][i]
    return result

def mult(M, N):
    if not is_possible(M, N):
        return []

    width, height = get_dims(M, N)
    result = []
    

    for j in range(height):
        result.append([])
        for i in range(width):
            result[j].append(get_element_at(M, N, i, j))

    return result
