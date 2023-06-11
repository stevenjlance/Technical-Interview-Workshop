def solution(s):
    # Create a variable to hold the final result
    result = ""
    # Iterate through the string
    for i in range(len(s)):
        # If the letter is uppercase, add a space before it and then add the lowercase version of the letter
        if s[i].isupper():
            result += " "
        result += s[i].lower()
    # Return the final result, but remove any leading or trailing spaces we may have added in.
    return result.strip()

""""
# Example
For s = "CodesignalIsAwesome", the output should be
solution(s) = "codesignal is awesome";
For s = "Hello", the output should be
solution(s) = "hello".
"""

print(solution("CodesignalIsAwesome"))