def subpatterns(astring):
    return f"The string '{astring}' contains {len([sub for sub in [astring[start:end] for start in range(len(astring)) for end in range(start + 3, len(astring) + 1)] if len([1 for i in range(len(sub) - 1) if sub[i] < sub[i + 1]]) - len([1 for i in range(len(sub) - 1) if sub[i] > sub[i + 1]]) == 0])} substring patterns."
