def rec_hof(hofs, lst): return lst if len(hofs) == 0 else hofs[0][0](hofs[0][1], [rec_hof(hofs[1:], x) for x in lst]) # "os one-liners do Miguel" :(
