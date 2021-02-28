def override(l1, l2): return sorted(l2 + [t for t in l1 if not any(t[0] == el[0] for el in l2)]) # "os one-liners do Miguel" :(
