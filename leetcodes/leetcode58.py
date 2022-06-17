def lengthOfLastWord():
    s = '   fly me   to   the moon  '
    t = s.split(' ')
    i = -1
    while True:
        if len(t[i]) == 0:
            i -=1
        else:
            return len(t[i])

print(lengthOfLastWord())