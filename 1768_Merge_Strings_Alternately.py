from time import perf_counter_ns
def mergeAlternately(word1: str, word2: str) -> str:
        string = ''
        for n in range(max(len(word1),len(word2))):
            try:
                string += (word1[n])
            except IndexError:
                pass
            try:
                string += (word2[n])
            except IndexError:
                pass
        return string

start = perf_counter_ns()
print(mergeAlternately("abc", "pqr"))
print(f"{perf_counter_ns() - start} ns")