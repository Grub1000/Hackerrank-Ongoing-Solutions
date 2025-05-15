n = int(input())
nIntegers =  list(map(lambda a: int(a), input().split()))
nIntegersAny = list(map(lambda a: any([a > 0]) , nIntegers))
if all(nIntegersAny):
    palindromic = False
    for i in range(n):
        if  str(nIntegers[i]) == str(nIntegers[i])[::-1]:
            palindromic = True
            break
    print(palindromic)
else:
    print("False")


# Challenge: Same solution in 2 lines below...
# n, nIntegers = int(input()), list(map(lambda a: int(a), input().split()))
# print("True") if all(list(map(lambda a: any([a > 0]) , nIntegers))) and any(list(map(lambda a: str(a) == str(a)[::-1], nIntegers))) else print("False")
# Challenge: Same solution in 2 lines above

# Sample Input: 
# 5
# 12 9 61 5 14

# Sample Output: 
# True