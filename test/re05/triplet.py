def triplet(a_tuple):
    for i in range(len(a_tuple)):
        for j in range(i + 1, len(a_tuple)):
            for k in range(j + 1, len(a_tuple)):
                if a_tuple[i] + a_tuple[j] + a_tuple[k] == 0:
                    return (a_tuple[i], a_tuple[j], a_tuple[k])
    return ()
