def sparse_dot_product(dict1, dict2): return sum([dict1.get(i, 0) * dict2.get(i, 0) for i in dict1]) # "os one-liners do Miguel" :(
