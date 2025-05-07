xk = input()                                     # Get x and k
p = list(input())                                # Get Polynomial function P
for i in range(len(p)):                          # For every occurrance of x in P, Replace x with the value x from xk pair
    if p[i] == "x":
        p[i] = xk[0]
print(eval("".join(p)) == int(xk.split(" ")[1])) # Evaluate the solution after replacing the variables with integer x and compare with k for the answer T or F


# Task
# You are given a polynomial  P of a single indeterminate (or variable), .
# You are also given the values of x and k . Your task is to verify if P(x) = k.

# Constraints
# All coefficients of polynomial P are integers.
# x and y are also integers.

# Input Format
# The first line contains the space separated values of x and k.
# The second line contains the polynomial P.

# Output Format
# Print True if P(x) = k. Otherwise, print False.

# Sample Input
# 1 4
# x**3 + x**2 + x + 1

# Sample Output
# True


