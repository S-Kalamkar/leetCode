from collections import defaultdict
def characterReplacement(s: str, k: int) -> int:
        n = len(s)
        l = 0
        counts = defaultdict(int)
        answer = 0
        for r in range(n):
            counts[s[r]] += 1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            answer = max(answer, r - l + 1)

        return answer
