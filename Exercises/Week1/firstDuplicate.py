def solution(a):
    seen = set()
    for num in a:
        if num in seen:
            return num
        seen.add(num)
    return -1

""""
# Example
For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be solution(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be solution(a) = -1.


"""

print(solution([2, 1, 3, 5, 3, 2]))