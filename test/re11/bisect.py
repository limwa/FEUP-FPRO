def bisect(f, n, lower = 0, upper = 1, calc = lambda f, n, lower, upper, mid: round(mid, 5) if n == 1 else bisect(f, n - 1, mid, upper) if f(mid) * f(lower) > 0 else bisect(f, n - 1, lower, mid)): return calc(f, n, lower, upper, (lower + upper) / 2) # "os one-liners do Miguel" :(