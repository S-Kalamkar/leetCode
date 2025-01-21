def calPoints(operations: list[str]) -> int:
    scores = []
    total = 0
    for operation in operations:
        if operation == "C":
            total -= scores.pop()
        elif operation == "D":
            double = scores[-1]*2
            scores.append(double)
            total += double
        elif operation == "+":
            added = scores[-1]+scores[-2]
            scores.append(added)
            total += added
        else:
            scores.append(int(operation))
            total += int(operation)
    return total