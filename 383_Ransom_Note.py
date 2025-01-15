from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ranCounter = Counter(ransomNote)
        magCounter = Counter(magazine)


        for letter, count in zip(ranCounter.keys(), ranCounter.values()):
            if count > magCounter[letter]:
                 return False
        return True

print(canConstruct("aa", "aa"))
        
        

