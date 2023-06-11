def solution(a):
    # # newArr;
    result = []
    # Make empty 2D array
    for i in range(len(a)):
        result.insert(0, [])
    # Iterate through and put each number in the sub array in the 2D array. Place each value in the front of the sub array.
    for arr in a:
        for index, val in enumerate(arr):
            result[index].insert(0, val)
    return result

"""
Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

solution(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

"""
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))