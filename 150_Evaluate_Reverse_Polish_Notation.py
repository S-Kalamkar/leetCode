def evalRPN(tokens: list[str]) -> int:
        stack = []
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: y - x, 
            '*': lambda x, y: x * y, 
            '/': lambda x, y: int(y / x)
        }
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                stack.append(operations[token](stack.pop(), stack.pop()))

        return stack.pop()