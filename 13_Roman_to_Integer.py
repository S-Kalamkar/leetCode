def romanToInt(s: str) -> int:
    n = len(s)
    values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    total = 0
    i = 0
    for k in range(n):
        if i < n:
            if s[i:i + 2] in values:
                total += values.get(s[i:i + 2])
                i += 2
                if i > n:
                    break
            else:
                total += values.get(s[i])
                i += 1
    return total
print(romanToInt("VI"))