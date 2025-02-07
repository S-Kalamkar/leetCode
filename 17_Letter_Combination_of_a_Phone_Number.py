def letterCombinations(digits: str) -> list[str]:
    n = len(digits)
    if n == 0:
        return []
    digiMap = {
                '2' : ['a', 'b', 'c'],
                '3' : ['d', 'e', 'f'], 
                '4' : ['g', 'h', 'i'], 
                '5' : ['j', 'k', 'l'], 
                '6' : ['m', 'n', 'o'], 
                '7' : ['p', 'q', 'r', 's'], 
                '8' : ['t', 'u', 'v'], 
                '9' : ['w', 'x', 'y', 'z']
            }
    ans = []
    def recur(size, currComb):
        if size == 0:
            ans.append("".join(currComb))
            return
        
        for l in range(len(digiMap[digits[size - 1]])):
            currComb.insert(0, digiMap[digits[size - 1]][l])
            recur(size - 1, currComb)
            currComb.remove(digiMap[digits[size - 1]][l])
    recur(n, [])
    
    return ans