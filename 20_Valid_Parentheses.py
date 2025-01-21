def isValid(s: str) -> bool:
    stack = []
    hashmap = {')':'(', ']':'[', '}':'{'}
    for i in s:
        if i not in hashmap:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] != hashmap[i]:
                return False
            stack.pop()
    return (len(stack) == 0)