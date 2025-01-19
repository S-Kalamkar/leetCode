from collections import Counter
def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        return min(counts['l']//2, counts['o']//2, counts['b'], counts['a'], counts['n'])