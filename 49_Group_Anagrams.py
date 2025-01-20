from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            anagram_dict["".join(sorted(word))] += [word]
        return list(anagram_dict.values())
