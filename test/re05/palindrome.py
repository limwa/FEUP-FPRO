def is_palindrome(s):
    return s == s[::-1]

def palindrome(s):
    result = 0

    length = len(s)
    for start in range(length - 1):
        for end in range(start + 2, length + 1):
            if is_palindrome(s[start:end]):
                result += 1

    return "The string '{0}' contains {1} palindrome substrings.".format(s, result)
