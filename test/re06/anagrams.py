def anagrams(l):
    d = {}
    for word in l.copy():
        letters = "".join(sorted(list(word.lower().replace(" ", ""))))
        if letters in d:
            d[letters].append(word)
        else:
            d[letters] = [word]

    values = [sorted(x, key=lambda x: x.lower()) for x in list(d.values())]
    values.sort(key=lambda x: x[0].lower())
    return values
