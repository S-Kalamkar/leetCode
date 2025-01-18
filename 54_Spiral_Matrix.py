def spiralOrder(matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        output = []
        i, j = 0, 0
        UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
        direction = RIGHT
        upWall = 0
        rightWall = n
        downWall = m
        leftWall =  -1
        while len(output) != m*n:
            if direction == RIGHT:
                while j < rightWall:
                    output.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                rightWall -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < downWall:
                    output.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                downWall -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > leftWall:
                    output.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                leftWall += 1
                direction = UP
            else:
                while i > upWall:
                    output.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                upWall += 1
                direction = RIGHT
        return output