def flatten(it): return flatten(sum([[i] if not isinstance(i, list) else i for i in it], start=[])) if any([isinstance(i, list) for i in it]) else it # "os one-liners do Miguel" :(
