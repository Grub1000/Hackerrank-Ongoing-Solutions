regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))




# Input Format:
# A single line of input containing a string of Roman characters.

# Output Format:
# Output a single line containing True or False according to the instructions above.















