def brute_force(f, l): return [x for x in map("".join, __import__('itertools').product(l, repeat=3)) if f(x)] # "os one-liners do Miguel" :(
