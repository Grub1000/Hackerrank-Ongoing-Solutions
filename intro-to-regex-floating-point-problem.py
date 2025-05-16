import re
n = int(input())
for i in range(n):
    value = input()
    if  (value == "0"):
        print("False")
    elif (re.match("^[+-]?\d*\.?\d+$", value)):
        print("True")
    else:
        print("False")


# Sample Input:
# 4
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff

# Sample Output:
# False
# True
# True
# False



