# 35ms Runtime Attempt
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterIndex = {}
        longestSubstringLength = 0
        for i in s:
            if i in characterIndex:
                # Inclusive delete of characterIndex keys up to the repeated letter.
                # We transform the dictonary / hashmap into a list of keys and then use the index value of the repeated character to slice
                # the list up to and including that character from left to right. Example: [:4] ~ This would mean to slice and remove items
                # at the 0,1,2,3 positions.
                for key in list(characterIndex.keys())[:list(characterIndex).index(i) + 1]: 
                    del characterIndex[key]
                    print(characterIndex)
                characterIndex[i] = 1
            else:
                characterIndex[i] = 1
                if longestSubstringLength < len(characterIndex):
                    longestSubstringLength = len(characterIndex)
        return longestSubstringLength

solution = Solution()
# solution.lengthOfLongestSubstring("abcabcabc")
print(solution.lengthOfLongestSubstring("aabaab!bb"))

# Description:
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# 5ms Runtime Example:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exist = {}
        maxi = 0 
        i = 0 
        for j in range(len(s)):
            if(s[j] in exist and exist[s[j]] >= i ):
                i = exist[s[j]] + 1
            exist[s[j]]= j
            maxi = max(maxi,j-i+1)
            
        return maxi

# Explanation
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Maps:
        # character -> most recent index where it appeared
        exist = {}

        # Stores the longest valid substring we've seen so far.
        #
        # IMPORTANT:
        # This is NOT the length of the current window.
        #
        # It is the BEST answer we've found at ANY point
        # during the algorithm.
        #
        # Example:
        #
        # "abcabcbb"
        #
        # Window lengths become:
        #
        # 1 -> 2 -> 3 -> 3 -> 3 -> 3 -> 2 -> 1
        #
        # maxi remembers the largest one (3)
        # even after the window later shrinks.
        maxi = 0

        # Left side of our sliding window.
        #
        # Think of i as saying:
        #
        # "Everything BEFORE this index has already
        # been discarded and can never be part of the
        # current valid substring."
        #
        # Window always represents:
        #
        # s[i : j+1]
        #
        # Invariant:
        # Every character inside this window is unique.
        i = 0

        # j expands the window one character at a time.
        for j in range(len(s)):

            # If we've seen this character before AND
            # that previous occurrence is still inside
            # our current window...
            if s[j] in exist and exist[s[j]] >= i:

                # ...then we have found a duplicate.
                #
                # Instead of moving i one step at a time,
                # we can JUMP directly after the previous
                # occurrence.
                #
                # Example:
                #
                # a b c d a
                # ^       ^
                #
                # Previous 'a' is at index 0.
                #
                # Every substring beginning at index 0
                # through index 4 is invalid because it
                # contains two 'a's.
                #
                # So we immediately discard everything
                # up to and including that old 'a':
                #
                # b c d a
                # ^
                #
                # i becomes:
                i = exist[s[j]] + 1

            # Record the newest position of this character.
            exist[s[j]] = j

            # Current window length.
            #
            # Since the window is inclusive:
            #
            # i .......... j
            #
            # length = right - left + 1
            current_length = j - i + 1

            # If the current window is larger than
            # any we've seen before, update our answer.
            #
            # Notice something really clever:
            #
            # We NEVER need to remember old windows.
            #
            # As soon as a window is no longer the
            # largest, we don't care about it anymore.
            #
            # We simply keep the maximum length seen
            # throughout the entire scan.
            maxi = max(maxi, current_length)

        return maxi


