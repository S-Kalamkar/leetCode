def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                return True
                
            
        if matrix[m][0] > target:
            m -= 1
        i = m


        l, r = 0, len(matrix[i]) - 1

        while l <= r:
            m = (l + r) // 2
            
            if matrix[i][m] < target:
                l = m + 1
            elif matrix[i][m] > target:
                r = m - 1
            else:
                return True
        return False