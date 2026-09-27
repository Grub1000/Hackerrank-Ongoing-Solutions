def longestPalindrome(inputString: str) -> str:
    # palindromicSubstringDict = {}
    longestPalindromicSubstring = ""
    stringLength = len(inputString)
    currentSubstringWindowLength = 1 
    index = 0
    while currentSubstringWindowLength < stringLength + 1:
        tempString = inputString[index : currentSubstringWindowLength]
        # print(tempString)
        if tempString[::-1] == tempString and len(tempString) > len(longestPalindromicSubstring):
            longestPalindromicSubstring = tempString
        index += 1
        if index == currentSubstringWindowLength:
            index = 0
            currentSubstringWindowLength += 1
    print(longestPalindromicSubstring)

longestPalindrome("a")


# An Improvement to this to make it substantiall 
# faster would be to make it go in reverse. This 
# way we simply need to find the largest palindrome
# while skipping all of the smaller palindromes.
