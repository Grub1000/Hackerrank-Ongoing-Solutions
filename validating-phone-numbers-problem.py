import re

n = int(input())
for i in range(n):
    phoneNumber = input()
    if re.match(r'[789]\d{9}$', phoneNumber):
        print("YES")
    else:
        print("NO")


# Input Format:
# The first line contains an integer N, the number of inputs.
# N lines follow, each containing some string.


# Sample Input:
# 2
# 9587456281
# 1252478965

# Sample Output:
# YES
# NO



















