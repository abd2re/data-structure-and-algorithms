'''{}()[] return True'''
'''{] return False'''
'''][ return False'''
'''([)] return False'''
'''([{}]) return True'''



def isvalid():
    v = '()()()()()()()'
    priority = []

    hashmap = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    for sym in v:
        if sym in hashmap.keys():
            priority.append(hashmap[sym])
        if sym in hashmap.values():
            if not priority:
                return 'Invalid'
            if priority[-1] != sym:
                return 'Invalid'
            priority.pop()

    return 'valid'


print(isvalid())



