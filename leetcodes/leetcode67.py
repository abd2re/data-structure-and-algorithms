a = "11"
b = "1"
import math as m

def addBinary(a,b):
    sum1 = 0

    for i,num in enumerate(reversed(a)):
        if num == '1':
            sum1 += 2**i

    for i,num in enumerate(reversed(b)):
        if num == '1':
            sum1 += 2**i

    if sum1 == 0:
        return '0'

    t = ''
    l = m.floor(m.log(sum1,2))

    for i in range(l,-1,-1):
        if sum1 - 2**i >= 0:
            t += '1'
            sum1 -= 2**i
        else:
            t += '0'
    return t




addBinary(a,b)