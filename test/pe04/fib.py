def fib(start, end, fibs={ 1: 1, 2: 1 }): yield from [fibs.get(i) or fibs.__setitem__(i, fibs[i - 1] + fibs[i - 2]) or fibs.get(i) for i in range(1, end + 1)][start - 1:] # "os one-liners do Miguel" :(
