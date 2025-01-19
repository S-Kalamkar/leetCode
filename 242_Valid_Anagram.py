def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for l in set(s):
            if s.count(l) != t.count(l):
                return False
        return True