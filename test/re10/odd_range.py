def odd_range(start, stop, step): return (x for x in range(start if start % 2 != 0 else start + 1, stop, 2 * step)) # "os one-liners do Miguel" :(
