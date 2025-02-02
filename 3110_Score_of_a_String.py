def scoreOfString(s: str) -> int:
    total = 0
    for l in range(len(s) - 1):
        r = l + 1
        total += abs(ord(s[l]) - ord(s[r]))
    return total
    