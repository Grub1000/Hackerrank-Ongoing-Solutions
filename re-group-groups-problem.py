import re
inputFixed = re.sub(r'[^a-zA-Z0-9]', '', input())
m = re.search( r"(\w)\1", inputFixed)
if m == None:
    print(-1)
else:
    print(m.group()[0])


# Task:
# You are given a string .
# Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.
# If no repetitions output -1

# Sample Input:
# ..12345678910111213141516171820212223

# Sample Output:
# 1
