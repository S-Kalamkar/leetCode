def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    stack = []
    output = [0] * n

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            output[j] = i - j

        stack.append(i)
    return output

        