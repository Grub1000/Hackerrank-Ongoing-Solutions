import re

N = int(input())

for i in range(N):
    uID = "".join(sorted(input()))
    # print(uID)
    if (len(uID) == 10 and
        re.match(r'', uID) and 
        re.search(r'[A-Z]{2}', uID) and
        re.search(r'\d\d\d', uID) and
        not re.search(r'[^a-zA-Z0-9]', uID) and
        not re.search(r'(.)\1', uID)):
        print("Valid")
    else:
        print("Invalid")

# Task:
# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.
# A valid UID must follow the rules below:
# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0 - 9).
# It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.

# Sample Input
# 2
# B1CD102354
# B1CDEF2354

# Sample Output
# Invalid
# Valid
