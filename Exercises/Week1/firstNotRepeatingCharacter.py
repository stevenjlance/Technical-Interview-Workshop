def solution(s):
    count = {}
    for letter in s:
        if letter not in count:
            count[letter] = 1
        else:
            update = count[letter] + 1
            count[letter] = update
    moreThanOne = []
    for letter in count:
        if count[letter] == 1:
            moreThanOne.append(letter)
    if len(moreThanOne) == 0:
        return "_"
    minIndex = 100000
    for letter in moreThanOne:
        if s.index(letter) < minIndex:
            minIndex = s.index(letter)
    return s[minIndex]

""""
# Example
For s = "abacabad", the output should be
solution(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
solution(s) = '_'.

There are no characters in this string that do not repeat.

"""

print(solution("abacabad"))