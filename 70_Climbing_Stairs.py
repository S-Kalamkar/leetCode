def climbStairs(n):
    a = 1
    b = 1
    for i in range(n):
        b, a = a + b, b
    return a