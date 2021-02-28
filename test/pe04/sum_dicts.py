def sum_dicts(lst): return { key: sum(aux.get(key, 0) for aux in lst) for d in lst for key in d.keys() } # "os one-liners do Miguel" :(
