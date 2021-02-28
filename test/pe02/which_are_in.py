def which_are_in(l1, l2): return sorted([s1 for s1 in l1 if any([s1 in s2 for s2 in l2])]) # "os one-liners do Miguel" :(
