def rec_count(alist, result={}): return ([result.__setitem__(key, result.get(key, 0) + 1) if not isinstance(key, list) else rec_count(key) for key in alist] and None) or result # "os one-liners do Miguel" :(
