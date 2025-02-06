def combine(n: int, k: int) -> list[list[int]]:
        if k > n:
            return
        
        if n == 1:
                if k == 1:
                    return [[1]]
            
        pool = tuple(range(1, n + 1))
        indices = list(range(k))
        ans = []
        
        ans.append([list(pool[i] for i in indices)])
        while True:
            for i in reversed(range(k)):
                if indices[i] != i + n - k:
                    break
            else:
                return ans
            indices[i] += 1
            for j in range(i + 1, k):
                indices[j] = indices[j - 1] + 1
            ans.append(list(pool[i] for i in indices))
