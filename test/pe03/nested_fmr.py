def nested_fmr(f, m, r, lst): return __import__('functools').reduce(r, map(m, filter(f, (nested_fmr(f, m, r, x) if isinstance(x, list) else x for x in lst)))) # "os one-liners do Miguel" :(
