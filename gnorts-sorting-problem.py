stringInput = input()
charList = []
charListUpper = []
charListNumberOdd = []
charListNumberEven = []
for i in stringInput:
    if (ord(i) > 47 and ord(i) < 58):
        if(int(i) % 2 == 0):
            charListNumberEven.append(i)
        else:
            charListNumberOdd.append(i)
    if (ord(i) > 64 and ord(i) < 91):
        charListUpper.append(i)
    if (ord(i) > 96 and ord(i) < 123):
        charList.append(i)
result = "".join(sorted(charList)) + "".join(sorted(charListUpper)) + "".join(sorted(charListNumberOdd)) + "".join(sorted(charListNumberEven))
print(result)

# Sample Input: 
# Sorting1234

# Sample Output: 
# ginortS1324