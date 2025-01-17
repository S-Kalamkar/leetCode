def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    
    firstWord = strs[0]
    end = 0
    for i in range(len(firstWord)):
        for word in strs[1:]:
            if i == len(word) or firstWord[i] != word[i]:
                return firstWord[:end]
        end += 1

    return firstWord
       