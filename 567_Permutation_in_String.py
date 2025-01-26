from collections import defaultdict

def checkInclusion(s1: str, s2: str) -> bool:
        windowLen = len(s1)
        n = len(s2)

        if windowLen > n:
            return False

        counts1 = defaultdict(int)
        counts2 = defaultdict(int)
        
        for i in s1:
            counts1[i] += 1
                
        for i in range(windowLen - 1):
            counts2[s2[i]] += 1
            if not counts1[s2[i]]:
                counts1[s2[i]] = 0
                
        for i in range(windowLen - 1, n):
            counts2[s2[i]] += 1
            if not counts1[s2[i]]:
                counts1[s2[i]] = 0
            
            if counts1 == counts2:
                return True
                
            counts2[s2[i - windowLen + 1]] -= 1
            
            
        return False