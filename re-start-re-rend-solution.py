import re
S = input()
k = input()
regex = r'(?=(' + k + '))'
m = re.finditer(regex, S)
# print(m)

count = 0
for i in m:
    print( "(" + str(i.start()) + ", " +  str(i.start() + (len(k) - 1)) + ")" )
    count += 1
if count == 0:
    print("(-1, -1)")


# Task:
# You are given a string .
# Your task is to find the indices of the start and end of string  in .
# 
# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).

# Sample Input:
# aaadaa
# aa
# 
# Sample Output:
# (0, 1)
# (1, 2)
# (4, 5)
# 





