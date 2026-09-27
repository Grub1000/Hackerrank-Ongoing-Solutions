# 8998ms Runtime
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

longestPalindrome("babad")

# Optimization Hypothesis:
#
# An Improvement to this to make it substantially faster would be to make it go in reverse. This 
# way we simply need to find the largest palindrome while skipping all of the smaller palindromes.




# 4015ms Runtime
def reverseLongestPalindrome(inputString: str) -> str:
    # longestPalindromicString = ""
    stringLength = len(inputString)
    currentSubstringWindowLength = stringLength
    index = 0
    while currentSubstringWindowLength > 0:
        tempString = inputString[index : index + currentSubstringWindowLength]
        # print(tempString)
        if tempString[::-1] == tempString:
            print(tempString)
            return tempString
            break
        elif index + currentSubstringWindowLength == stringLength:
            # print("removed length")
            index = 0
            currentSubstringWindowLength -= 1
        else:
            # print("incremented")
            index += 1
            # currentSubstringWindowLength += 1
    # return longestPalindromicString
        
reverseLongestPalindrome("babad")      

# Optimization Result:
#
# My initial Hypothesis on runtime improvement was correct. This reverse implementation resulted in a 50% runtime reduction.