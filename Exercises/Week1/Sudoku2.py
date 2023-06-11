def solution(grid):
    # Check row
    for arr in grid:
        if(checkArr(arr) == False): return False
    # Check column
    for col in range(9):
        found = set()
        for row in range(9):
            num = grid[row][col]
            if num == ".": continue
            if num in found:
                return False
            found.add(num)
    # Check sub grid (3 x 3 area)
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            # Create a subgrid for 3 x 3 area
            subgrid = [grid[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
            # Check subgrid
            if(checkArr(subgrid) == False): return False
    # Passed all 3? Return true
    return True

def checkArr(arr):
    found = set()
    for num in arr:
        if num == ".": continue
        if num in found:
            return False
        found.add(num)