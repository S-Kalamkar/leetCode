def isSubsequence(s: str, t: str) -> bool:
    s = list(s)
    n = len(t)
    for i in range(n):
        if len(s) == 0:
            return True
        if t[i] == s[0]:
            s.pop(0)
    return len(s) == 0
