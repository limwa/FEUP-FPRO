def sort_leaders(records):
    return tuple([tuple(j) for j in sorted([list(i) for i in records], key=lambda record: (-max(record[1]), len(record[1]), record[0].lower()))])
