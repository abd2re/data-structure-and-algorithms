# valid parentheses
s ="(){}}{"
def isValid(s):

    hashmap = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    if len(s) < 2 or s[0] in hashmap.values():
        return False
    priority = []
    for i in s:
        if i in hashmap.keys():
            priority.append(hashmap[i])
        if i in hashmap.values():
            if not priority:
                return False
            if priority[-1] != i:
                return False
            priority = priority[:-1]

    if not priority:
        return True
    return False




print(isValid(s))