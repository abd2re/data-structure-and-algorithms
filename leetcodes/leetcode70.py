def climbStairs():
    n = 6
    a, b = 1, 1
    for i in range(n):
        b, a = a + b, b

    return a






print(climbStairs())




