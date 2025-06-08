import re
n = int(input())

fullText = ""
for i in range(n):
    fullText += input() + '\n'
print(re.sub(r'(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)', lambda i: "and" if i.group() == "&&" else "or", fullText))






