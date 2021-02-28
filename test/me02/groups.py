def groups(students):
    return tuple([(students[i], students[j], students[k]) for i in range(len(students)) for j in range(i + 1, len(students)) for k in range(j + 1, len(students))])
