def insert(array, i, e):
    array.insert(i, e)
    return ""

def _print(array):
    return str(array) + " "

def remove(array, e):
    if e in array:
        array.remove(e)
    return ""

def append(array, e):
    array.append(e)
    return ""

def sort(array):
    array.sort()
    return ""

def pop(array):
    array.pop()
    return ""

def reverse(array):
    array.reverse()
    return ""

commands = {
    "insert": insert,
    "print": _print,
    "remove": remove,
    "append": append,
    "sort": sort,
    "pop": pop,
    "reverse": reverse
}

def manipulator(l, cmds):
    result = ""
    for cmd in cmds:
        parts = cmd.split()
        verb = parts[0]

        result += commands[verb](l, *[int(e) for e in parts[1:]])
    return result
