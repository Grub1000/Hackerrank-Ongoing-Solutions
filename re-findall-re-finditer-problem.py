
import re

pattern = r'(?i)([aeiou]{2,})(?=[^aeiou])'

text = input()

matches = re.findall(pattern, text)
for i in matches:
    print(i)
if len(matches) == 0:
    print(-1)

# Task:
# You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of  that contains  or more vowels.
# Also, these substrings must lie in between  consonants and should contain vowels only.

# Sample Input:
# rabcdeefgyYhFjkIoomnpOeorteeeeet

# Sample Output:
# ee
# Ioo
# Oeo
# eeeee