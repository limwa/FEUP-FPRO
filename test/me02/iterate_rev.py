def iterate_rev(names, numbers, emails):
    return "\n".join(reversed([" - ".join([str(x) for x in i]) for i in zip(names, numbers, emails)]))
