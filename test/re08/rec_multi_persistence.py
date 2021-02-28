def rec_multiplicative_persistence(n): return 0 if n < 10 else 1 + rec_multiplicative_persistence(__import__('math').prod([int(i) for i in list(str(n))])) # "os one-liners do Miguel" :(
