import re

patternStart = r'^'
patternNoRepetition = r'(?!.*(\d)(-?\1){3})'
creditCardPattern = r'[456]((\d){15}|(\d){3}(-[\d]{4}){3})'
patternEnd = r'$'

pattern = re.compile(
    patternStart
    + patternNoRepetition
    + creditCardPattern
    + patternEnd
)

for i in range(int(input())):
    creditCardNum = input()
    print("Valid" if pattern.search(creditCardNum) else 'Invalid')

# Sample Input
# 6
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456

# Sample Output
# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid