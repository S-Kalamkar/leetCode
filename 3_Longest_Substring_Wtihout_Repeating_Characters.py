def lengthOfLongestSubstring(s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        l = 0
        longest = 0
        seen = set()
        for r in range(n):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])

                    l += 1
                l += 1
            else:
                seen.add(s[r])
                longest = max(longest, r - l + 1)
        return longest if longest > 0 else n
                

